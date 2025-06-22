import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key= os.getenv("OPENAI_API_KEY")

def read_component(file_path):
    """
    Read the content of a JSX/TSX component file.

    :param file_path: Path to the JSX/TSX file.
    :return: Content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_prompt():
    """
    Read the content of a prompt file.

    :param prompt_path: Path to the prompt file.
    :return: Content of the prompt file as a string.
    """
    with open("prompts/testng_pom_prompt.txt", 'r', encoding='utf-8') as file:
        return file.read()

def generate_test_code(component_code):
    prompt_template = read_prompt()
    full_prompt = f"{prompt_template}\n\nReact component code:\n{component_code[:3000]}"
    print("[INFO] Sending prompt to AI...")
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful Automation Testing assistant."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.3
    )
    generated_code = response.choices[0].message.content.strip()
    print("[✅] Test generated!\n")
    print(generated_code)
    return generated_code

if __name__ == "__main__":
    component_file_path = "D:/Technical/Tech_Learning/Repos/full-stack-with-react-and-spring-boot/frontend/todo-app/src/components/todo/LoginComponent.jsx"
    component = read_component(component_file_path)
    print("[INFO] Component code read successfully.")

    test_code = generate_test_code(component)

    # Save the generated test code to a file
