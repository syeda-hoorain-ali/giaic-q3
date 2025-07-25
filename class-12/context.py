import asyncio
from dataclasses import dataclass
import os
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, RunContextWrapper, Runner, function_tool

load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.0-flash"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)

# -------------------- Context class --------------------
@dataclass
class User:
    id: int
    name: str
    age: int


# -------------------- Tool to get data from context --------------------    

@function_tool
def get_user_age(ctx: RunContextWrapper[User]):
    """Return user's age"""
    return f"{ctx.context.name} is {ctx.context.age} years old."

# -------------------- Main agent --------------------    

agent = Agent(
    name="Agent",
    instructions="You are a helpful assistant. Use the tools provided to answer questions.",
    model=model,
    tools=[get_user_age],
)


async def main():
    try:
        user = User(123, "Hoorain", 40)
        result = await Runner.run(
            starting_agent=agent,
            input="What is user's age?",
            context=user,
        )

        print(result.final_output)
    except Exception as e:
        print("\n you cannot use tools with structue output on same agent using gemini model")
        print(f"An Error occured: {e}")


if __name__ == "__main__":
    asyncio.run(main())
