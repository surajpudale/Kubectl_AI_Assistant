# Kubectl AI Assistant

A modern, interactive, and visually appealing web-based assistant for Kubernetes, powered by Azure OpenAI and `kubectl-ai`. This project lets you manage and troubleshoot your Kubernetes clusters using natural language, with a beautiful dashboard UI and persistent chat history.

---

## ✨ Features

- **Conversational AI for Kubernetes**: Ask questions or give commands in plain English, and get real-time answers or actions on your cluster.
- **Attractive Web Dashboard**: Responsive, full-screen UI with a side menu of prompt suggestions and a chat panel.
- **Prompt Suggestions**: Clickable, customizable prompt suggestions to help you get started quickly.
- **Persistent Chat History**: See your full conversation history on the right, even after page reloads (server-side persistence).
- **Table & Color Formatting**: Kubernetes output is cleaned and formatted for easy reading.
- **Reset Conversation**: Start fresh with a single click.
- **Easy to Extend**: Modular Python codebase, ready for new features or integrations.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/surajpudale/Kubectl_AI_Assistant.git
cd Kubectl_AI_Assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prerequisites

- Python 3.8+
- [kubectl-ai](https://github.com/robusta-dev/kubectl-ai) installed and in your PATH
- Access to your Kubernetes cluster (via `kubectl` context)
- Access to Azure OpenAI (see below)

### 4. Set Azure OpenAI Environment Variables

Set these environment variables in your shell or in `run.py` before running the app:

```bash
export AZURE_OPENAI_API_KEY="<your-azure-openai-api-key>"
export AZURE_OPENAI_ENDPOINT="<your-azure-openai-endpoint>"
export OPENAI_DEPLOYMENT_NAME="o4-mini"
```

Or edit the defaults in `run.py`.

### 5. Run the App

```bash
python run.py
```

Open your browser to [http://localhost:5000](http://localhost:5000)

---

## 🖥️ Project Structure

```
your-project-root/
│
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── routes.py           # All Flask routes and logic
│   ├── utils.py            # Utility functions
│   ├── templates/
│   │   └── index.html      # Jinja2 HTML template
│   └── static/             # (Optional) CSS, JS, images
│
├── run.py                  # Entry point to run the app
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🧑‍💻 Usage

- **Type or click a prompt** in the left menu (e.g., `list pods`, `create namespace mynamespace`).
- **Chat history** appears on the right and is persistent as long as the server is running.
- **Reset Conversation** to clear the chat and start over.
- **All output** is formatted for readability, including tables and logs.

---

## 🛠️ Customization & Extensibility

- Add more prompt suggestions in `routes.py` or make them dynamic.
- Add authentication, multi-user support, or advanced analytics.
- Integrate with other Kubernetes tools or cloud providers.
- Style the dashboard further in `templates/index.html` and `static/`.

---

## 🤝 Contributing

Pull requests, issues, and suggestions are welcome! Please open an issue or PR to discuss improvements or new features.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [kubectl-ai](https://github.com/robusta-dev/kubectl-ai)
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Flask](https://flask.palletsprojects.com/)

---

> Made with ❤️ for Kubernetes and AI enthusiasts.