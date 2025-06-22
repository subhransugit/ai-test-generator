from git import Repo
import os

def clone_repo(repo_url, target_path=r"D:\Technical\Tech_Learning\Repos\full-stack-with-react-and-spring-boot"):
    """
    Clone a Git repository to a specified target path.

    :param repo_url: URL of the repository to clone.
    :param target_path: Local path where the repository will be cloned.
    """
    if os.path.exists(target_path):
        print("[INFO] Repo already exists")
    else:
        print(f"[INFO] Cloning repo{repo_url}...")
        Repo.clone_from(repo_url, target_path)
        print("[SUCCESS] Repo cloned.")



if __name__ == "__main__":
    clone_repo("https://github.com/in28minutes/full-stack-with-react-and-spring-boot")
