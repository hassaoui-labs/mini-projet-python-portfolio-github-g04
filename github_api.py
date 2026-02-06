import requests


class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self, token=None):
        self.headers = {
            "Accept": "application/vnd.github+json"
        }
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get_repos(self, username):
        url = f"{self.BASE_URL}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_commits(self, username, repo_name, limit=100):
        url = f"{self.BASE_URL}/repos/{username}/{repo_name}/commits"
        params = {"per_page": limit}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
