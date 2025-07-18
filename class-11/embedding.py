# How to create Vector Database
# Go to Open AI Platform -> Dashboard -> storage -> vector stores -> 
# create db -> add files -> upload your file -> attach -> copy vector store id and save it

import asyncio
from agents import Agent, Runner, FileSearchTool

agent = Agent(
    name="Assistant",
    instructions="""
        You are acting as me, the owner of this service. 
        Always speak in the first person, as if you are the person providing the service. 
        Be friendly, concise, and helpful. Clearly explain what I offer, answer questions, 
        and keep the conversation natural and tailored to the user's needs. 
        Ask clarifying questions if needed to better assist them.
    """,
    tools=[
        FileSearchTool( # FileSearchTool will only work with OpenAI API key,
            max_num_results=3,
            vector_store_ids=["YOUR_VECTOR_STORE_ID"],
        )
    ]
)

async def main():
    result = await Runner.run(agent, input="what is your name")
    print(result.final_output)
    

asyncio.run(main())
