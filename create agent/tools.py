import os
from dotenv import load_dotenv
from autogen import ConversableAgent,register_function
from pydantic import BaseModel, Field


load_dotenv()

llm_config = { "config_list": [{ "model": "gpt-4o", "api_key": os.getenv("AZURE_OPENAI_API_KEY"),"base_url":os.getenv("AZURE_OPENAI_BASE_URL"),"api_type":"azure","api_version":"2025-01-01-preview" }] }

from typing import Annotated, Literal

Operator = Literal["+", "-", "*", "/"]



class CalculatorInput(BaseModel):
    a: Annotated[int, Field(description="The first number.")]
    b: Annotated[int, Field(description="The second number.")]
    operator: Annotated[Operator, Field(description="The operator.")]


def calculator(input: Annotated[CalculatorInput, "Input to the calculator."]) -> int:
    if input.operator == "+":
        return input.a + input.b
    elif input.operator == "-":
        return input.a - input.b
    elif input.operator == "*":
        return input.a * input.b
    elif input.operator == "/":
        return int(input.a / input.b)
    else:
        raise ValueError("Invalid operator")

# def calculator(a: int, b: int, operator: Annotated[Operator, "operator"]) -> int:
#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a - b
#     elif operator == "*":
#         return a * b
#     elif operator == "/":
#         return int(a / b)
#     else:
#         raise ValueError("Invalid operator")

# Let's first define the assistant agent that suggests tool calls.
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with simple calculations. "
    "Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# # Register the tool signature with the assistant agent.
# assistant.register_for_llm(name="calculator", description="A simple calculator")(calculator)

# # Register the tool function with the user proxy agent.
# user_proxy.register_for_execution(name="calculator")(calculator)


# Register the calculator function to the two agents.
register_function(
    calculator,
    caller=assistant,  # The assistant agent can suggest calls to the calculator.
    executor=user_proxy,  # The user proxy agent can execute the calculator calls.
    name="calculator",  # By default, the function name is used as the tool name.
    description="A simple calculator",  # A description of the tool.
)

chat_result = user_proxy.initiate_chat(assistant, message="What is (44232 + 13312 / (232 - 32)) * 5?")
