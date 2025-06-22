from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0.3)

def generate_refactored_test(component_code, existing_test_code):
    prompt = f"""
You are an expert in Selenium + TestNG with Java.

Given:
- A modified React component
- An existing TestNG test class

Regenerate or refactor the Java test class appropriately.
❗ Do not include any explanation. 
❗ Respond with ONLY the full Java test class inside a code block (using triple backticks).

React Component:
{component_code[:3000]}

Existing Java Test Class:
{existing_test_code[:3000]}
"""
    response = llm.invoke(prompt)
    return response.content
