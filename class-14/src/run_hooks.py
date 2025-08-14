import asyncio
import os
from agents import (
    Agent, RunHooks, Runner, function_tool, 
    set_default_openai_api, set_default_openai_client, set_tracing_disabled
)
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI


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

# Simple Run Hooks - tracks EVERYTHING in the run
class MyRunnerHooks(RunHooks):
    async def on_agent_start(self, context, agent):
        # print(f">> {agent.name} started.")
        print("on_agent_start in runner hooks:", agent.name)

    async def on_agent_end(self, context, agent, output):
        # print(f">> {agent.name} finished.")
        print("on_agent_end in runner hooks:", agent.name)

    async def on_tool_start(self, context, agent, tool):
        # print(f">> Agent {agent.name} call {tool.name}.")
        print("on_tool_start in runner hook", agent.name, tool.name)

    async def on_tool_end(self, context, agent, tool, result):
        # print(f">> Tool {tool.name} excecuted.")
        print("on_tool_end in runner hook", agent.name, tool.name)
        print("Tool Result:", result)


# Simple tools
@function_tool
def check_order():
    """Check order status"""
    return "Order #123 is on the way!"

@function_tool
def check_refund():
    """Check refund status"""
    return "Refund of $50 processed!"


# Create TWO agents no hooks on agent
agent1 = Agent(
    name="Order Agent",
    instructions="Check order status",
    tools=[check_order],
    model="gemini-2.0-flash",
    # NOTE: NO hooks on this agent
)

agent2 = Agent(
    name="Refund Agent",
    instructions="Check refund status",
    tools=[check_refund],
    model="gemini-2.0-flash",
    # NOTE: NO hooks on this agent
)


async def main():
    print('=' * 50)
    print("RUN HOOKS DEMO")
    print('=' * 50)
    print()

    # Create runner hooks
    run_hooks = MyRunnerHooks()

    # Run 1: Order Agent
    print("📦 Checking order...")
    result1 = await Runner.run(
        starting_agent=agent1,
        input="Check my order",
        hooks=run_hooks,
    )
    print(f"\n[ANSWER] {result1.final_output}")


    # Run 2: Refund Agent (same hooks can track this too!)
    print("\n💰 Checking refund...")
    result2 = await Runner.run(
        starting_agent=agent2,
        input="Check my refund",
        hooks=run_hooks, # <- SAME HOOKS ON THIS RUN
    )

    print(f"\n[ANSWER] {result2.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
