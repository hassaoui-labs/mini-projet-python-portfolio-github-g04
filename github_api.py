import requests
from config import GITHUB_TOKEN, BASE_URL


HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_user_repos(username):
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"{BASE_URL}/users/{username}/repos"
        params = {"per_page": per_page, "page": page}

        try:
            r = requests.get(url, headers=HEADERS, params=params, timeout=10)
        except requests.RequestException as e:
            print("Erreur connexion API:", e)
            return []

        if r.status_code != 200:
            print("Erreur API:", r.status_code)
            print(r.text)
            return []

        data = r.json()
        if not isinstance(data, list) or len(data) == 0:
            break

        repos.extend(data)
        page += 1

    return repos


def get_repo_commits(username, repo):
    commits = []
    page = 1
    per_page = 100

    while True:
        url = f"{BASE_URL}/repos/{username}/{repo}/commits"
        params = {"per_page": per_page, "page": page}

        try:
            r = requests.get(url, headers=HEADERS, params=params, timeout=10)
        except requests.RequestException:
            return []

        if r.status_code != 200:
            return []

        data = r.json()
        if not isinstance(data, list) or len(data) == 0:
            break

        commits.extend(data)
        page += 1

    return commits


def get_languages(username, repo):
    url = f"{BASE_URL}/repos/{username}/{repo}/languages"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
    except requests.RequestException:
        return {}

    if r.status_code != 200:
        return {}

    data = r.json()
    return data if isinstance(data, dict) else {}
