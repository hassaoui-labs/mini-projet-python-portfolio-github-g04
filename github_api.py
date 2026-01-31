import requests
from config import GITHUB_TOKEN, BASE_URL

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Erreur API:", r.status_code)
        print(r.text)
        return []

    return r.json()
def get_repo_commits(username, repo):
    url = f"{BASE_URL}/repos/{username}/{repo}/commits"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return []
    return r.json()


def get_languages(username, repo):
    url = f"{BASE_URL}/repos/{username}/{repo}/languages"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return {}
    return r.json()
