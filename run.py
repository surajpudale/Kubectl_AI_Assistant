import os
from app import create_app

# Set Azure OpenAI environment variables here for generic use
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY", "<your-azure-openai-api-key>")
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT", "<your-azure-openai-endpoint>")
os.environ["OPENAI_DEPLOYMENT_NAME"] = os.getenv("OPENAI_DEPLOYMENT_NAME", "<your-deployment-name>")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
