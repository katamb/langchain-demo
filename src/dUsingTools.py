from dotenv import load_dotenv, find_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL


if __name__ == "__main__":
    load_dotenv(find_dotenv())  # OPENAI_API_KEY variable is defined there

    prompt = PromptTemplate(input_variables=["tools", "tool_names", "input", "agent_scratchpad"], template="""
Answer the following questions as best you can. You have access to the following tool:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be {tool_names}
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question:{input}
Thought:{agent_scratchpad}
    """)
    # Choose the LLM to use
    llm = OpenAI()
    # Create tools
    python_repl = PythonREPL()
    repl_tool = Tool(
        name="python_repl",
        description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
        func=python_repl.run,
    )
    tools = [repl_tool]
    # Construct the ReAct agent
    agent = create_react_agent(llm, tools, prompt)
    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    output = agent_executor.invoke({"input": "The tourists are accommodated in 3 hotels. There are 8 more tourists in the second hotel than in the first hotel and in the third hotel there are 14 more tourists than in the second one. If there is a total of 258 tourists, how many tourists are accommodated in each of the hotels? Lets think step-by-step. First try to figure out the response without tools and then use tools to check the correctness of the response."})
    print(output["output"])
