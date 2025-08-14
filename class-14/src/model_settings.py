import os
from agents import (
    Agent, ModelSettings, OpenAIChatCompletionsModel, Runner, function_tool, 
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

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=external_client)

set_default_openai_client(external_client)
set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")


# 🛠️ Simple tool for learning
@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    area = length * width
    return f"Area = {length} × {width} = {area} square units"


def main():
    """Learn Model Settings with simple examples."""
    # 🎯 Example 1: Temperature (Creativity Control)
    print("\n❄️🔥 Temperature Settings")
    print("-" * 30)
    
    agent_cold = Agent(
        name="Cold Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.1),
        model=model
    )
    
    agent_hot = Agent(
        name="Hot Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=1.9),
        model="gemini-2.0-flash"
    )
    
    question = "Tell me about AI in 2 sentences"
    
    print("Cold Agent (Temperature = 0.1):")
    result_cold = Runner.run_sync(agent_cold, question)
    print(result_cold.final_output)
    
    print("\nHot Agent (Temperature = 1.9):")
    result_hot = Runner.run_sync(agent_hot, question)
    print(result_hot.final_output)
    
    print("\n💡 Notice: Cold = focused, Hot = creative")
    print("📝 Note: Gemini temperature range extends to 2.0")
    
    # 🎯 Example 2: Tool Choice
    print("\n🔧 Tool Choice Settings")
    print("-" * 30)
    
    agent_auto = Agent(
        name="Auto",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="auto"),
        model="gemini-2.0-flash"
    )
    
    agent_required = Agent(
        name="Required",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="required"),
        model="gemini-2.0-flash"
    )

    agent_none = Agent(
        name="None",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="none"),
        model="gemini-2.0-flash"
    )
    
    question = "What's the area of a 5x3 rectangle?"
    
    print("Auto Tool Choice:")
    result_auto = Runner.run_sync(agent_auto, question)
    print(result_auto.final_output)
    
    print("\nRequired Tool Choice:")
    result_required = Runner.run_sync(agent_required, question)
    print(result_required.final_output)

    print("\nNone Tool Choice:")
    result_none = Runner.run_sync(agent_none, question)
    print(result_none.final_output)
    
    print("\n💡 Notice: Auto = decides, Required = must use tool")


if __name__ == "__main__":
    main()
