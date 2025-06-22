import os
import re

def extract_java_classes(text):
    """
    Extract all Java class blocks from LLM output.
    """
    code_blocks = re.findall(r"```(?:java)?(.*?)```", text, re.DOTALL)
    cleaned_classes = []
    for block in code_blocks:
        if "public class" in block:
            cleaned_classes.append(block.strip())
    return cleaned_classes

def save_test_files(llm_response, output_dir="./generated-tests"):
    os.makedirs(output_dir, exist_ok=True)
    classes = extract_java_classes(llm_response)

    for java_code in classes:
        try:
            match = re.search(r"public class (\w+)", java_code)
            if not match:
                print("[⚠️] Could not find class name.")
                continue
            class_name = match.group(1)
            file_path = os.path.join(output_dir, class_name + ".java")
            with open(file_path, "w") as f:
                f.write(java_code)
            print(f"[💾] Saved: {file_path}")
        except Exception as e:
            print(f"[ERROR] Failed to write file: {e}")

if __name__ == "__main__":
    # Example use after running generate_tests.py
    from generate_tests import generate_test_code, read_component

    file_path = r"D:\Technical\Tech_workspace\full-stack-with-react-and-spring-boot\frontend\todo-app\src\components\todo\LoginComponent.jsx"
    component_code = read_component(file_path)
    generated_code = generate_test_code(component_code)
    save_test_files(generated_code)

