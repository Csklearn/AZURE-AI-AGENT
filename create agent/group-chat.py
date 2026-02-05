import os
from dotenv import load_dotenv
from autogen import ConversableAgent,GroupChat,GroupChatManager
import pprint
load_dotenv()

llm_config = { "config_list": [{ "model": "gpt-4o", "api_key": os.getenv("AZURE_OPENAI_API_KEY"),"base_url":os.getenv("AZURE_OPENAI_BASE_URL"),"api_type":"azure","api_version":"2025-01-01-preview" }] }

import os


# The Number Agent always returns the same numbers.
number_agent = ConversableAgent(
    name="Number_Agent",
    system_message="You return me the numbers I give you, one number each line.",
    human_input_mode="NEVER",
    llm_config=llm_config
)

# The Adder Agent adds 1 to each number it receives.
adder_agent = ConversableAgent(
    name="Adder_Agent",
    system_message="You add 1 to each number I give you and return me the new numbers, one number each line.",
    human_input_mode="NEVER",
    llm_config=llm_config,

)

# The Multiplier Agent multiplies each number it receives by 2.
multiplier_agent = ConversableAgent(
    name="Multiplier_Agent",
    system_message="You multiply each number I give you by 2 and return me the new numbers, one number each line.",
    human_input_mode="NEVER",
    llm_config=llm_config
)

# The Subtracter Agent subtracts 1 from each number it receives.
subtracter_agent = ConversableAgent(
    name="Subtracter_Agent",
    system_message="You subtract 1 from each number I give you and return me the new numbers, one number each line.",
    human_input_mode="NEVER",
    llm_config=llm_config
)

# The Divider Agent divides each number it receives by 2.
divider_agent = ConversableAgent(
    name="Divider_Agent",
    system_message="You divide each number I give you by 2 and return me the new numbers, one number each line.",
    human_input_mode="NEVER",
    llm_config=llm_config
)

# Start a sequence of two-agent chats.
# Each element in the list is a dictionary that specifies the arguments
# for the initiate_chat method.
# chat_results = number_agent.initiate_chats
# (
#     [
#         {
#             "recipient": adder_agent,
#             "message": "14",
#             "max_turns": 1,
#             "summary_method": "last_msg",
#         },
#         {
#             "recipient": multiplier_agent,
#             "message": "These are my numbers",
#             "max_turns": 1,
#             "summary_method": "last_msg",
#         },
#         {
#             "recipient": subtracter_agent,
#             "message": "These are my numbers",
#             "max_turns": 1,
#             "summary_method": "last_msg",
#         },
#         {
#             "recipient": divider_agent,
#             "message": "These are my numbers",
#             "max_turns": 1,
#             "summary_method": "last_msg",
#         },
#     ]
# )

# The `description` attribute is a string that describes the agent.
# It can also be set in `ConversableAgent` constructor.
adder_agent.description = "Add 1 to each input number."
multiplier_agent.description = "Multiply each input number by 2."
subtracter_agent.description = "Subtract 1 from each input number."
divider_agent.description = "Divide each input number by 2."
number_agent.description = "Return the numbers given."



group_chat = GroupChat(
    agents=[adder_agent, multiplier_agent, subtracter_agent, divider_agent, number_agent],
    messages=[],
    max_round=6,
    send_introductions=True
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
    
)

chat_result = number_agent.initiate_chat(
    group_chat_manager,
    message="My number is 3, I want to turn it into 13.",
    summary_method="reflection_with_llm",
)
