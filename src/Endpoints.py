import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate


app = FastAPI()


class CodeSnippet(BaseModel):
    code: str

class CodeRequest(BaseModel):
    request: str
    language: str

class CodeTranslation(BaseModel):
    code: str
    desired_language: str

class StyleCode(BaseModel):
    code: str
    desired_style: str



@app.post("/explain_code")
async def explain(code: str):
    model = Ollama(model="deepseek-r1:1.5b")

    prompt = PromptTemplate.from_template(
        "Explain this code {code}"
    )

    chain = prompt | model

    explanation = chain.invoke({
        "code": code,
    })
    return {"explanation": explanation}



@app.post("/generate_code")
async def generate(request: str, language: str):
    model = Ollama(model="deepseek-r1:1.5b")

    prompt = PromptTemplate.from_template(
        "Generate {language} code for this requirement:\n\n{request}"
    )

    chain = prompt | model

    generated_code = chain.invoke({
        "language": language,
        "description": request
    })

    return {"language": language, "code": generated_code}


@app.post("/translate_code")
async def translate(code: str, desired_language: str):
    model = Ollama(model="deepseek-r1:1.5b")

    prompt = PromptTemplate.from_template(
        "Transform this code:{code} into {desired_language}"
    )


    chain = prompt | model
    translated_code=chain.invoke({
        "code": code,
        "desired_language": desired_language,
    })
    return {"translated_code": translated_code}


@app.post("/style_preferences")
async def style(code: str, desired_style: str):
    model = Ollama(model="deepseek-r1:1.5b")

    prompt = PromptTemplate.from_template(
        "Change the style,naming conventions etc of this code: {code} based on this: {desired_style}"
    )


    chain = prompt | model

    styled_code=chain.invoke({
        "code": code,
        "desired_style": desired_style,
    })
    return {"styled_code": styled_code}

@app.post("/code_quality_analysis")
async def code_quality_analysis(code: str):
    model = Ollama(model="deepseek-r1:1.5b")

    prompt = PromptTemplate.from_template(
        "In detail describe the quality, good and bad things about the following code: {code}"
    )

    chain = prompt | model

    codequality_analysis = chain.invoke({
        "code": code,
    })
    return {"code_quality_analysis": codequality_analysis}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

