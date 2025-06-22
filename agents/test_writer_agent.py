import os
import re
import shutil

def extract_java_classes(text):
    code_blocks = re.findall(r"```(?:java)?(.*?)```", text, re.DOTALL)
    cleaned_classes = []
    for block in code_blocks:
        if "public class" in block:
            cleaned_classes.append(block.strip())
    return cleaned_classes

def write_and_copy_tests(llm_response, gen_dir:str ="./generated-tests", test_project_dir:str ="../functional-tests/src/test/java"):
    os.makedirs(gen_dir, exist_ok=True)
    pages_dir = os.path.join(test_project_dir, "pages")
    tests_dir = os.path.join(test_project_dir, "tests")
    os.makedirs(pages_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)

    classes = extract_java_classes(llm_response)

    for java_code in classes:
        try:
            match = re.search(r"public class (\w+)", java_code)
            if not match:
                print("[⚠️] Could not find class name.")
                continue

            class_name = match.group(1)
            filename = class_name + ".java"
            file_path = os.path.join(gen_dir, filename)

            with open(file_path, "w") as f:
                f.write(java_code)
            print(f"[💾] Generated: {file_path}")

            # Copy to test project
            if "Page" in class_name:
                shutil.copy(file_path, os.path.join(pages_dir, filename))
            elif "Test" in class_name:
                shutil.copy(file_path, os.path.join(tests_dir, filename))
            else:
                shutil.copy(file_path, os.path.join(test_project_dir, filename))

            print(f"[📂] Copied to functional-tests: {class_name}")

        except Exception as e:
            print(f"[❌] Error writing or copying: {e}")
