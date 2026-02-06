from github_api import get_repo_commits, get_languages


def analyze_repo(username, repo):
    repo_name = repo.get("name")

    commits = get_repo_commits(username, repo_name)
    commit_count = len(commits) if isinstance(commits, list) else 0

    langs = get_languages(username, repo_name)
    lang_list = list(langs.keys()) if isinstance(langs, dict) else []

    stars = repo.get("stargazers_count", 0)
    forks = repo.get("forks_count", 0)

    score = commit_count * 2 + stars * 5 + forks * 3

    return {
        "name": repo_name,
        "commits": commit_count,
        "languages": lang_list,
        "stars": stars,
        "forks": forks,
        "score": score,
        "url": repo.get("html_url"),
    }


def analyze_all(username, repos):
    results = []

    for repo in repos:
        if not repo.get("fork", False):
            results.append(analyze_repo(username, repo))

    return results
