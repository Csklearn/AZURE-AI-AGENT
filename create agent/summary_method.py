import os
from dotenv import load_dotenv
from autogen import ConversableAgent
import pprint
load_dotenv()

llm_config = { "config_list": [{ "model": "gpt-4o", "api_key": os.getenv("AZURE_OPENAI_API_KEY"),"base_url":os.getenv("AZURE_OPENAI_BASE_URL"),"api_type":"azure","api_version":"2025-01-01-preview" }] }

import os


student_agent = ConversableAgent(
    name="Student_Agent",
    system_message="You are a student willing to learn.",
    llm_config=llm_config,
)
teacher_agent = ConversableAgent(
    name="Teacher_Agent",
    system_message="You are a math teacher.",
    llm_config=llm_config,
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    message="What is triangle inequality?",
    summary_method="reflection_with_llm",
    max_turns=2,
)

print(chat_result.summary)
pprint.pprint(chat_result.chat_history)
