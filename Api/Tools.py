from langchain.tools import Tool
from langchain_community.llms import Ollama
import requests
from Endpoints import CodeRequest, CodeSnippet, CodeTranslation, StyleCode


def recognize_language(codesnippet: CodeSnippet):
    obj = {"codesnippet": codesnippet.code, "language": "string"}
    response = requests.post('http://ai.easv.dk:8989/tools/langrecog/?temp=0', json=obj)
    return response.json()

recognize_language = Tool(
    name="RecognizeLanguage",
    func=lambda inputs: recognize_language(inputs["codesnippet"]),
    description="Recognizes the language of a given code snippet."
)


def explain_code(codesnippet: CodeSnippet):
    obj = {"code": codesnippet.code}
    response=requests.post("http://localhost:8000/explain_code", json=obj)
    return response.json()

explain_code = Tool(
    name="ExplainCode",
    func=lambda inputs: explain_code(inputs["codesnippet"]),
    description="Explains the language of a given code snippet."
)

def generate_code(request: CodeRequest):
    obj = {"language": request.language, "description": request.request}
    response=requests.post("http://localhost:8000/generate_code", json=obj)
    return response.json()

generate_code = Tool(
    name="GenerateCode",
    func=lambda inputs: generate_code(inputs["request"]),
    description="Generates the code of a given request."
)

def translate_code(request: CodeTranslation):
    obj = {"code": request.code, "desired_language": request.language}
    response=requests.post("http://localhost:8000/translate_code", json=obj)
    return response.json()

translate_code = Tool(
    name="TranslateCode",
    func=lambda inputs: translate_code(inputs["request"]),
    description="Translates the code of a given request to another coding language."
)

def style_change(request: StyleCode):
    obj = {"code": request.code, "desired_style": request.desired_style}
    response=requests.post("http://localhost:8000/style_preferences", json=obj)
    return response.json()

style_change = Tool(
    name="StyleChange",
    func=lambda inputs: style_change(inputs["request"]),
    description="Changes the code of a given request to the given style preference."
)

def code_quality_analyzer(request: CodeSnippet):
    obj = {"code": request.code}
    response=requests.post("https://localhost:8000/code_quality_analysis", json=obj)
    return f"Analyzing quality of the given code:\n{response.json()}"

codeQualityTool = Tool(
    name="CodeQualityAnalyzer",
    func=lambda inputs: code_quality_analyzer(inputs["request"]),
    description="Analyzes the quality and potential improvements in a given code snippet."
)

