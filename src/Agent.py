from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
from src.Tools import explainTool,generateTool,translateTool,styleTool,codeQualityTool

def chooseModel(request_type: str):
    models = {
        "explain_code": "llama3.2",
        "generate_code": "deepseek-r1:1.5b",
        "translate_code": "llama3.2",
        "style_preferences": "llama3.2",
        "code_quality": "deepseek-r1:1.5b",
    }
    return Ollama(model=models.get(request_type, "deepseek-r1:1.5b"))





def run_agent(task_type: str, input_data: str):
    agent = initialize_agent(
        tools=[explainTool, generateTool, translateTool, styleTool, codeQualityTool],
        llm=chooseModel(task_type),
        verbose=True
    )
    #llm = chooseModel()
    #agent.llm = llm

    tool_map = {
        "explain_code": explainTool,
        "generate_code": generateTool,
        "translate_code": translateTool,
        "style_preferences": styleTool,
        "code_quality": codeQualityTool,
    }

    tool = tool_map.get(task_type)
    if tool:
        return tool.invoke(input_data)
    else:
        return agent.invoke(input_data)
