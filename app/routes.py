import os
import re
import subprocess
import threading
from flask import Blueprint, render_template, request, jsonify, session

main = Blueprint('main', __name__)

conversation = []
conversation_lock = threading.Lock()
pending_confirmation = {"prompt": None, "session_prompt": None}

def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def format_table(text):
    lines = text.splitlines()
    if any(re.search(r'\s{2,}', line) for line in lines):
        return '<pre>' + '\n'.join(lines) + '</pre>'
    return text

def handle_prompt(prompt):
    try:
        # Use only supported flags and pass prompt as a single argument
        base_cmd = ["kubectl-ai", "--llm-provider=azopenai", "--model=o4-mini", prompt, "--quiet"]
        result = subprocess.run(
            base_cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60
        )
        output = result.stdout if result.returncode == 0 else result.stderr
        output = strip_ansi(output)
        output = format_table(output)
        return output
    except subprocess.TimeoutExpired:
        return "Error: The operation timed out. Please try a shorter or simpler prompt."
    except FileNotFoundError:
        return "Error: kubectl-ai is not installed or not in PATH."
    except KeyboardInterrupt:
        return "Session interrupted."

# Multi-step confirmation flow support
@main.route("/", methods=["GET", "POST"])
def index():
    global conversation
    if request.method == "POST":
        user_input = request.form["prompt"]
        # Remove all interactive/action_keywords logic
        if request.form.get("confirmation") == "true" and pending_confirmation["prompt"]:
            # User confirmed, proceed with the pending prompt plus user's confirmation response
            confirm_prompt = f"{pending_confirmation['prompt']}\n{user_input}"
            output = handle_prompt(confirm_prompt)
            with conversation_lock:
                conversation.append(f"User: {user_input}")
                conversation.append(f"Assistant: {output.strip()}" )
            pending_confirmation["prompt"] = None
            pending_confirmation["session_prompt"] = None
            return jsonify({"response": output, "confirmation_required": False})
        # Normal flow
        with conversation_lock:
            session_prompt = "\n".join(conversation + [user_input])
            output = handle_prompt(session_prompt)
            # Detect confirmation prompt in output
            if output and any(phrase in output.lower() for phrase in ["do you want to proceed", "please confirm", "shall i go ahead", "please confirm and let me know"]):
                pending_confirmation["prompt"] = user_input
                pending_confirmation["session_prompt"] = session_prompt + "\n" + user_input
                conversation.append(f"User: {user_input}")
                conversation.append(f"Assistant: {output.strip()}")
                return jsonify({"response": output, "confirmation_required": True})
            conversation.append(f"User: {user_input}")
            conversation.append(f"Assistant: {output.strip()}")
            return jsonify({"response": output, "confirmation_required": False})
    # Prepare history for rendering
    with conversation_lock:
        history = []
        for i in range(0, len(conversation), 2):
            user = conversation[i][len("User: "):] if i < len(conversation) else ""
            assistant = conversation[i+1][len("Assistant: "):] if i+1 < len(conversation) else ""
            history.append({"user": user, "assistant": assistant})
    return render_template("index.html", suggestions=[
        "list pods",
        "create namespace mynamespace",
        "get logs from pod nginx",
        "describe deployment myapp",
        "delete pod nginx",
        "scale deployment myapp --replicas=3"
    ], history=history)

@main.route("/reset", methods=["POST"])
def reset():
    global conversation
    with conversation_lock:
        conversation = []
        pending_confirmation = {"prompt": None, "session_prompt": None}
    return ("", 204)
