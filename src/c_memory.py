from dotenv import load_dotenv, find_dotenv
from langchain.globals import set_verbose
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain_core.prompts import PromptTemplate


if __name__ == "__main__":
    load_dotenv(find_dotenv())  # OPENAI_API_KEY variable is defined there
    set_verbose(True)
    template = """
    You are a security analyst explaining security vulnerabilities to management. 
    Please always answer with 1 sentence.
    {history}
    {input}
    """

    prompt = PromptTemplate(input_variables=["input", "history"], template=template)  # Create template object
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")  # Define which LLM to use. -> temp: between 0 and 1, the bigger the number, the more creative the LLM, models
    conversation = ConversationChain(llm=llm, prompt=prompt, memory=ConversationBufferMemory())  # By default is using ConversationBufferMemory
    q1 = "How would you explain to non-domain experts what the CWE-23 means and why it's important to fix this."
    llm_response = conversation.predict(input=q1)  # Call model with the given prompt and provide the variable
    print(llm_response)  # Output response

    # Continue conversation
    q2 = "Can you provide some more CWE-IDs that point to similar vulnerabilities?"
    llm_response2 = conversation.predict(input=q2)  # Call model with the given prompt and provide the variable
    print(llm_response2)  # Output response
