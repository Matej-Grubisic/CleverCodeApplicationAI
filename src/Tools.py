import json

from langchain.tools import Tool
import requests
from src.Endpoints import CodeRequest, CodeSnippet, CodeTranslation, StyleCode


def recognize_language(inputs_str:str)->str:
    inputs = json.loads(inputs_str)
    code = inputs["code"]
    obj = {"codesnippet": code, "language": "string"}
    response = requests.post('http://ai.easv.dk:8989/tools/langrecog/?temp=0', json=obj)
    return response.json()

recognizeTool = Tool(
    name="RecognizeLanguage",
    func=lambda inputs: recognize_language(inputs),
    description="Recognizes the language of a given code snippet."
)


def explain_code(inputs_str: str) -> str:

    inputs = json.loads(inputs_str)
    code = inputs["code"]

    obj = {"code": code}
    response=requests.post("http://localhost:8000/explain_code", json=obj)
    return response.json()

explainTool = Tool(
    name="ExplainCode",
    func=lambda inputs: explain_code(inputs),
    description="Explains the language of a given code snippet."
)

def generate_code(inputs_str: str) -> str:

    inputs = json.loads(inputs_str)
    request = inputs["request"]
    language = inputs["language"]

    obj = {"request": request,"language": language}
    response=requests.post("http://localhost:8000/generate_code", json=obj)
    return response.json()

generateTool = Tool(
    name="GenerateCode",
    func=lambda inputs: generate_code(inputs),
    description="Generates the code of a given request."
)

def translate_code(inputs_str: str) -> str:

    inputs = json.loads(inputs_str)
    code = inputs["code"]
    language = inputs["language"]

    obj = {"code": code, "desired_language": language}
    response=requests.post("http://localhost:8000/translate_code", json=obj)
    return response.json()

translateTool = Tool(
    name="TranslateCode",
    func=lambda inputs: translate_code(inputs),
    description="Translates the code of a given request to another coding language."
)

def style_change(inputs_str:str)->str:

    inputs = json.loads(inputs_str)
    code = inputs["code"]
    style = inputs["style"]


    obj = {"code": code, "desired_style": style}
    response=requests.post("http://localhost:8000/style_preferences", json=obj)
    return response.json()

styleTool = Tool(
    name="StyleChange",
    func=lambda inputs: style_change(inputs),
    description="Changes the code of a given request to the given style preference."
)

def code_quality_analyzer(inputs_str:str)->str:
    inputs = json.loads(inputs_str)
    code = inputs["code"]

    obj = {"code": code}
    response=requests.post("http://localhost:8000/code_quality_analysis", json=obj)
    return response.json()

codeQualityTool = Tool(
    name="CodeQualityAnalyzer",
    func=lambda inputs: code_quality_analyzer(inputs),
    description="Analyzes the quality and potential improvements in a given code snippet."
)

