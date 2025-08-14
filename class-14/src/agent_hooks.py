import asyncio
import os
from typing import Any
from agents import (
    Agent, AgentHooks, RunContextWrapper, Runner, Tool, function_tool, 
    set_default_openai_api, set_default_openai_client, set_tracing_disabled
)
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel


load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)
set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")


# Base model for context
class Order(BaseModel):
    order_id: str
    customer_name: str
    amount: float


# Simple Agent Hooks - track what one agent does
class SimpleAgentHooks(AgentHooks):
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """The agent is starting"""
        # print(f"[START] Agent '{agent.name}' started.")
        print("agent started during class")

    async def on_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        """This agent finished"""
        print(f"[END] Agent '{agent.name}' finished.")

    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool) -> None:
        """The agent is using tool"""
        # print(f"[TOOL START] Agent '{agent.name}' is using tool '{tool.name}'.")
        print("refund order tool started during class")

    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str) -> None:
        """The agent's tool finished'"""
        # print(f"[TOOL END] Tool '{tool.name}' done. Result: {result}")
        print("refund order tool finished during class")


# Simple tool - uses context wrapper
@function_tool
def refund_order(wrapper: RunContextWrapper[Order]):
    """Process a refund for the customer order"""
    print("refund_order tool is being called.")
    order = wrapper.context
    return f"Refund of ${order.amount} processed for order {order.order_id} (Customer: {order.customer_name})"

# Create hooks for our agent
my_hooks = SimpleAgentHooks()


# Create agent with hooks attached
support_agent = Agent(
    name="Support Bot",
    instructions="""You are a customer support agent. You must use the refund_order tool to process refunds.
    IMPORTANT: Always call the refund_order tool when someone ask about a refund. Do not just say you'll process it actually use the tool""",
    tools=[refund_order],
    model="gemini-2.0-flash",
    hooks=my_hooks # <- HOOKS ATTACHED TO THIS AGENT
)


async def main():
    print('=' * 50)
    print("AGENT HOOKS DEMO")
    print('=' * 50)

    # Create order context
    order = Order(
        order_id="ORD-12345",
        customer_name="Jhon Doe",
        amount=99.99,
    )

    # Run the agent with context
    result = await Runner.run(
        starting_agent=support_agent,
        input="I need a refund for my order. Please process my refund",
        context=order,
    )

    print(f"\n[ANSWER] {result.final_output}")

if __name__ == '__main__':
    asyncio.run(main())
