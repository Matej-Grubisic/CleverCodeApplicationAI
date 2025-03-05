from langchain.agents import initialize_agent
from langchain.llms import Ollama



def chooseModel(request_type:str):
    if request_type == "generation":
        return Ollama(model="deepseek-r1:1.5b")
    elif request_type == "explanation":
        return Ollama(model="llama3.2")
    elif request_type == "translation":
        return Ollama(model="llama3.2")
    elif request_type == "restyling":
        return Ollama(model="llama3.2")
    return Ollama(model="deepseek-r1:1.5b")


agent = initialize_agent(
    tools=[],
    llm=chooseModel,
    verbose=True
)