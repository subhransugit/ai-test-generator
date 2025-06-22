import argparse
import json
import os
import re

from agents.github_agent import clone_repo
from agents.jsx_extractor_agent import extract_jsx_files
from agents.prompt_generation_agent import generate_test_code
from agents.test_writer_agent import write_and_copy_tests
from agents.hash_registry import (
    get_file_hash, load_hash_registry, save_hash_registry,
    load_test_registry, save_test_registry
)
from agents.refactor_agent import generate_refactored_test

def run_pipeline(repo_url=None, frontend_path=None, output_dir=None):
    if not repo_url or not frontend_path:
        with open("config/settings.json") as f:
            config = json.load(f)
            repo_url = config["repo_url"]
            frontend_path = config["frontend_path"]
            output_dir = config.get("output_dir", "../functional-tests/src/test/java")


    repo_path = clone_repo(repo_url)
    jsx_files = extract_jsx_files(os.path.join(repo_path, frontend_path))

    hash_registry = load_hash_registry()
    test_registry = load_test_registry()

    for jsx in jsx_files:
        current_hash = get_file_hash(jsx)
        file_name = os.path.basename(jsx)

        with open(jsx, "r", encoding="utf-8") as f:
            component_code = f.read()

        if file_name in hash_registry and hash_registry[file_name] == current_hash:
            print(f"[SKIP] Unchanged: {file_name}")
            continue

        print(f"[🧠] Processing: {file_name}")

        if file_name in test_registry:
            test_class = test_registry[file_name]["test_class"]
            test_path = f"../functional-tests/src/test/java/tests/{test_class}.java"

            if os.path.exists(test_path):
                with open(test_path, "r", encoding="utf-8") as tf:
                    existing_test = tf.read()
                test_code = generate_refactored_test(component_code, existing_test)
            else:
                test_code = generate_test_code(component_code, file_name.replace(".jsx", ""))
        else:
            test_code = generate_test_code(component_code, file_name.replace(".jsx", ""))

        write_and_copy_tests(test_code, test_project_dir=output_dir)
        hash_registry[file_name] = current_hash

        matches = re.findall(r"public class (\w+)", test_code)
        test_class = [m for m in matches if "Test" in m]
        page_class = [m for m in matches if "Page" in m]

        test_registry[file_name] = {
            "test_class": test_class[0] if test_class else "UnknownTest",
            "page_class": page_class[0] if page_class else "UnknownPage"
        }

    save_hash_registry(hash_registry)
    save_test_registry(test_registry)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AI Test Generator Pipeline")
    parser.add_argument("--repo", type=str, help="GitHub repo URL to clone")
    parser.add_argument("--path", type=str, help="Frontend components path")
    parser.add_argument("--output", type=str, help="OutPut directory for generated tests")

    args = parser.parse_args()
    run_pipeline(repo_url=args.repo, frontend_path=args.path, output_dir=args.output)
