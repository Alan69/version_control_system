import os
import shutil
import datetime
import hashlib
import json

class VersionControlSystem:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo_meta_path = os.path.join(repo_path, ".vcs")
        self.commits_path = os.path.join(self.repo_meta_path, "commits")

        if not os.path.exists(self.repo_meta_path):
            os.makedirs(self.repo_meta_path)
            os.makedirs(self.commits_path)

    def initialize(self):
        print("Initializing VCS repository...")
        print(f"Repository path: {self.repo_path}")

    def add(self, file_path):
        print(f"Adding file to repository: {file_path}")
        shutil.copy(file_path, self.repo_path)

    def commit(self, message):
        print("Committing changes...")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        files = os.listdir(self.repo_path)
        commit_data = {
            "timestamp": timestamp,
            "message": message,
            "files": files
        }
        commit_hash = hashlib.sha1(json.dumps(commit_data).encode()).hexdigest()
        commit_file_path = os.path.join(self.commits_path, commit_hash)
        with open(commit_file_path, "w") as f:
            json.dump(commit_data, f, indent=4)
        print("Changes committed successfully.")

    def history(self):
        print("Commit History:")
        for commit_file in os.listdir(self.commits_path):
            with open(os.path.join(self.commits_path, commit_file), "r") as f:
                commit_data = json.load(f)
                print(f"Commit Hash: {commit_file}")
                print(f"Timestamp: {commit_data['timestamp']}")
                print(f"Message: {commit_data['message']}")
                print(f"Files: {commit_data['files']}")
                print()


# Example usage
if __name__ == "__main__":
    vcs = VersionControlSystem("my_repo")
    vcs.initialize()

    # Add files to repository
    vcs.add("file1.txt")
    vcs.add("file2.txt")

    # Commit changes
    vcs.commit("Initial commit")

    # View commit history
    vcs.history()
