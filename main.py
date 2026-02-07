import yaml
import github_api
import analyzer
import html_generator

# Charger config.yaml
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

username = config["github"]["username"]
token = config["github"].get("token")

client = github_api.GitHubClient(token)
repos = client.get_repos(username)

projects = []

for repo in repos:
    if config["filters"]["exclude_forks"] and repo["fork"]:
        continue

    commits = client.get_commits(
        username=username,
        repo_name=repo["name"],
        limit=100  # max 100 commits
    )

    project = analyzer.analyze_repo(repo, commits)
    projects.append(project)

html_generator.generate_html(projects, config)

print("✅ Portfolio généré avec succès")
