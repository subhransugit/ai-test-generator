
import hashlib
import json
import os

HASH_FILE = "file_hash_registry.json"
TEST_MAP_FILE = "generated_registry.json"

def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def load_hash_registry():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hash_registry(registry):
    with open(HASH_FILE, "w") as f:
        json.dump(registry, f, indent=2)

def load_test_registry():
    if os.path.exists(TEST_MAP_FILE):
        with open(TEST_MAP_FILE, "r") as f:
            return json.load(f)
    return {}

def save_test_registry(registry):
    with open(TEST_MAP_FILE, "w") as f:
        json.dump(registry, f, indent=2)
