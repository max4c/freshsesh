from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
import requests

class FetchThread(QThread):
    fetched = pyqtSignal(str)

    def __init__(self, num_commits, repo_name, owner, token):
        super().__init__()
        self.num_commits = num_commits
        self.repo_name = repo_name
        self.owner = owner
        self.token = token

    def run(self):
        data = self.fetch_data_from_api(self.num_commits, self.repo_name, self.owner, self.token)
        self.fetched.emit(data)

    def fetch_data_from_api(self, num_commits, repo_name, owner, token):
        # Convert num_commits to a numeric value if needed
        num_commits_map = {"last commit": 1, "last 2 commits": 2, "last 3 commits": 3}
        num_commits = num_commits_map.get(num_commits, 1)  # Default to 1 if no match

        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}"
        }
        api_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?per_page={num_commits}"

        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                commits = response.json()
                commit_messages = '\n'.join(commit["commit"]["message"] for commit in commits)
                return commit_messages
            else:
                return "Failed to fetch data from GitHub API"
        except Exception as e:
            return f"Error: {str(e)}"

class RecapGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.message_label = QLabel("Creating recap in...")
        self.layout.addWidget(self.message_label)
        self.setLayout(self.layout)

    def create_recap(self, num_commits, repo_name, owner="max4c", token="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"):
        self.fetch_thread = FetchThread(num_commits, repo_name, owner, token)
        self.fetch_thread.fetched.connect(self.update_ui)
        self.fetch_thread.start()

    def update_ui(self, data):
        self.message_label.setText(data)

if __name__ == "__main__":
    app = QApplication([])
    ui = RecapGUI()
    ui.show()
    ui.create_recap("last commit", "freshsesh")  # Adjust parameters as needed
    app.exec_()