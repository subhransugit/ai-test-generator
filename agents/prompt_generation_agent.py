import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI(model="gpt-4", temperature=0.3)

def load_prompt_template():


    with open("prompts/testng_pom_prompt.txt", 'r', encoding='utf-8') as file:
        return file.read()

def generate_test_code(component_code, component_name):
    prompt_template = load_prompt_template()
    filled_prompt = prompt_template.replace("<ComponentName>", component_name)
    full_prompt = f"{filled_prompt}\n\nReact Component:\n{component_code[:3000]}"
    response = llm.invoke(full_prompt)
    return response.content.strip()
