from datetime import datetime


def extract_commits(commits):
    formatted = []

    for commit in commits:
        commit_data = commit.get("commit", {})
        author_data = commit_data.get("author", {})

        date_iso = author_data.get("date")
        date = (
            datetime.fromisoformat(date_iso.replace("Z", ""))
            .strftime("%d/%m/%Y") if date_iso else "N/A"
        )

        formatted.append({
            "message": commit_data.get("message", "No message"),
            "author": author_data.get("name", "Unknown"),
            "date": date
        })

    return formatted


def analyze_repo(repo, commits):
    stars = repo["stargazers_count"]
    forks = repo["forks_count"]
    commit_count = len(commits)

    # Score simple et explicable
    score = (commit_count * 2)

    return {
        "name": repo["name"],
        "description": repo["description"] or "No description",
        "url": repo["html_url"],
        "language": repo["language"] or "N/A",
        "stars": stars,
        "forks": forks,
        "commit_count": commit_count,
        "score": score,
        "commits": extract_commits(commits)
    }
