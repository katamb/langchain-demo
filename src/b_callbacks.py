from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.globals import set_verbose
from langchain_core.prompts import PromptTemplate
from langchain_community.callbacks import get_openai_callback


if __name__ == "__main__":
    load_dotenv(find_dotenv())  # OPENAI_API_KEY variable is defined there
    set_verbose(True)
    template = """
    You are a security analyst explaining security vulnerabilities to management. 
    How would you explain to non-domain experts what the CWE {cwe-id} means and why it's important to fix this.
    Please answer with 5 sentences or less.
    """
    cwe_id = "CWE-23"

    prompt = PromptTemplate.from_template(template)
    # temp: between 0 and 1, the bigger the number, the more creative the LLM, models
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")
    with get_openai_callback() as cb:
        chain = LLMChain(llm=llm, prompt=prompt)
        llm_response = chain.invoke({"cwe-id": cwe_id})
        print("### The cost information ###")
        print(cb)

    print("\n### The result ###")
    print(llm_response["text"])
