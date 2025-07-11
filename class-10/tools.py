from agents import Agent, Runner, function_tool, WebSearchTool

@function_tool
def get_user_data(min_age: int) -> list[dict]:
    "Retrieve user data based on a minimum age"
    users = [
        {"name": "Muneeb", "age": 22},
        {"name": "Muhammad Ubaid Hussain", "age": 25},
        {"name": "Azan", "age": 19},
    ]

    for user in users:
        if user["age"] < min_age:
            users.remove(user)
    
    return users
    

rishtey_wali_agent = Agent(
    name="Auntie",
    model="gpt-4o-mini",
    instructions="You are a warm and wise 'Rishtey Wali Auntie' who helps people find matches",
    tools=[get_user_data, WebSearchTool()]   # WebSearchTool will only work with OpenAI API key, 
    # if you want to use any other free llm use "browser-use"
)

result = Runner.run_sync(
    starting_agent=rishtey_wali_agent, 
    input="find a match of 25 minimum age and tell me the details about the match from linkedin"
)

print(result.final_output)

