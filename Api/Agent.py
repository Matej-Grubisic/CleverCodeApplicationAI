from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
#from Tools import reconLanguage
#from Tools import codeQualityTool
from Tools import explain_code,generate_code,translate_code,style_change,code_quality_analyzer
from langchain.tools import Tool

def chooseModel(request_type: str):
    models = {
        "explain_code": "llama3.2",
        "generate_code": "deepseek-r1:1.5b",
        "translate_code": "llama3.2",
        "style_preferences": "llama3.2",
        "code_quality": "deepseek-r1:1.5b",
    }
    return Ollama(model=models.get(request_type, "deepseek-r1:1.5b"))


agent = initialize_agent(
    tools=[explain_code, generate_code, translate_code, style_change, code_quality_analyzer],
    llm=chooseModel("deepseek-r1:1.5b"),
    verbose=True
)


def run_agent(task_type: str, input_data: dict):
    llm = chooseModel(task_type)
    agent.llm = llm

    tool_map = {
        "explain_code": explain_code,
        "generate_code": generate_code,
        "translate_code": translate_code,
        "style_preferences": style_change,
        "code_quality": code_quality_analyzer,
    }

    tool = tool_map.get(task_type)
    if tool:
        return tool.invoke(input_data)
    else:
        return agent.invoke(input_data)
