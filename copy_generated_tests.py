import os
import shutil

# Source and target directories
generated_tests_dir = "./generated-tests"
functional_tests_dir = "../functional-tests/src/test/java"

# Target subfolders
pages_dir = os.path.join(functional_tests_dir, "pages")
tests_dir = os.path.join(functional_tests_dir, "tests")

# Ensure target folders exist
os.makedirs(pages_dir, exist_ok=True)
os.makedirs(tests_dir, exist_ok=True)

# Copy each generated .java file to correct subfolder
for filename in os.listdir(generated_tests_dir):
    if not filename.endswith(".java"):
        continue

    src_file = os.path.join(generated_tests_dir, filename)

    if "Page" in filename:
        dst_file = os.path.join(pages_dir, filename)
    elif "Test" in filename:
        dst_file = os.path.join(tests_dir, filename)
    else:
        dst_file = os.path.join(functional_tests_dir, filename)

    shutil.copyfile(src_file, dst_file)
    print(f"[✅] Copied: {filename} → {dst_file}")
