# LangChain
This is a demo project that displays some of the capabilities of LangChain. LangChain is an open-source framework designed for creating applications utilizing LLMs. It offers tools and abstractions, simplifying the process of working with LLMs. LangChain components can be used to construct new prompt chains or modify existing templates. Moreover, LangChain incorporates components enabling LLMs to access fresh data sets without necessitating retraining, with integrations utilising platforms like HuggingFace.

## Core components:
### Prompt templates (a)
Prompt templates are standardized structures for formatting queries consistently and accurately for AI models. The templates can be created and reused across different applications and language models.

### Callbacks (b)
Callbacks help to log, monitor, and stream specific events in LangChain operations.

### Memory (c)
Some conversational language model applications refine their responses with information recalled from past interactions. LangChain allows developers to include memory capabilities in their systems. It supports different memory structures.

### Agents (d)
LangChain provides tools and libraries to compose and customize chains. An agent is a special chain that prompts the language model to decide the best sequence in response to a query. When using an agent, developers provide the user's input, available tools, and possible intermediate steps to achieve the desired results. Then, the language model returns a viable sequence of actions the application can take.  

### Retrieval modules
LangChain helps to create RAG (Retrieval Augmented Generation) systems with numerous tools to transform, store, search, and retrieve information that refine the LLM responses. Can simplify working with vector databases and LLMs.


# Sources:
1. https://www.langchain.com/
2. https://python.langchain.com/docs
3. https://github.com/langchain-ai/langchain
4. https://aws.amazon.com/what-is/langchain/
