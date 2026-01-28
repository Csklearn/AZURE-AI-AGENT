import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent
load_dotenv()

llm_config = { "config_list": [{ "model": "gpt-4o", "api_key": os.getenv("AZURE_OPENAI_API_KEY"),"base_url":os.getenv("AZURE_OPENAI_BASE_URL"),"api_type":"azure","api_version":"2025-01-01-preview" }] }
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about NVDA and TESLA stock prices.",
)
