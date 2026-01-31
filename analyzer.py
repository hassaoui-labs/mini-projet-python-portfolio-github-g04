from github_api import get_repo_commits, get_languages

def analyze_repo(username, repo):

    repo_name = repo["name"]

    commits = get_repo_commits(username, repo_name)
    commit_count = len(commits) if isinstance(commits, list) else 0

    langs = get_languages(username, repo_name)
    lang_list = list(langs.keys())

    score = commit_count*2 + repo["stargazers_count"]*5 + repo["forks_count"]*3

    return {
        "name": repo_name,
        "commits": commit_count,
        "languages": lang_list,
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "score": score,
        "url": repo["html_url"]
    }


def analyze_all(username, repos):

    results = []

    for repo in repos:
        if not repo["fork"]:
            results.append(analyze_repo(username, repo))

    return results
