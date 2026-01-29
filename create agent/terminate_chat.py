import os
from dotenv import load_dotenv
from autogen import ConversableAgent,UserProxyAgent
load_dotenv()

llm_config = { "config_list": [{ "model": "gpt-4o", "api_key": os.getenv("AZURE_OPENAI_API_KEY"),"base_url":os.getenv("AZURE_OPENAI_BASE_URL"),"api_type":"azure","api_version":"2025-01-01-preview" }] }
assistant = ConversableAgent("assistant",system_message="You are helpful assitant guides booking airline ticket", llm_config=llm_config,human_input_mode="NEVER")
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False,human_input_mode="NEVER"
                              ,is_termination_msg=lambda msg:"terminate" in msg["content"].lower())

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me airlines availables from india to NewYork and mention terminate",
)

# Chat Level Config max_turn
# Agent Level Config max_consecutive_auto_reply is_termination_msg
