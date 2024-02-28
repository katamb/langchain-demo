from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate


if __name__ == "__main__":
    load_dotenv(find_dotenv())  # OPENAI_API_KEY variable is defined there
    template = """
    You are a security analyst explaining security vulnerabilities to management. 
    How would you explain to non-domain experts what the CWE {cwe-id} means and why it's important to fix this.
    Please answer with 3 sentences or less.
    """
    cwe_ids = ["CWE-23", "CWE-36"]

    prompt = PromptTemplate.from_template(template)  # Create template object
    # temp: between 0 and 1, the bigger the number, the more creative the LLM
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")  # Define which LLM to use
    chain = LLMChain(llm=llm, prompt=prompt)  # Bind prompt with LLM model
    for cwe_id in cwe_ids:
        llm_response = chain.invoke({"cwe-id": cwe_id})  # Call model with the given prompt and provide the variable
        print(llm_response["text"])  # Output response

