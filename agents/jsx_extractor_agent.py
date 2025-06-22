import os

def extract_jsx_files(base_path=r"D:\Technical\Tech_Learning\Repos\full-stack-with-react-and-spring-boot\frontend\todo-app\src"):
    """
    Extract all JSX component files from the specified base path.

    :param base_path: The directory to search for JSX components.
    :return: A list of paths to JSX component files.
    """
    print(f"[INFO] Extracting JSX/TSX files from {base_path}")
    jsx_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.jsx') or file.endswith('.tsx'):
                full_path = os.path.join(root, file)
                jsx_files.append(full_path)
                print(f"[INFO] Found JSX/TSX file: {full_path}")
    print(f"[SUCCESS] TOtal components Found: {len(jsx_files)}")

    return jsx_files
