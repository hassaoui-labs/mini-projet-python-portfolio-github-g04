from github_api import get_user_repos
from analyzer import analyze_all
from html_generator import generate_portfolio

username = input("GitHub username: ")

repos = get_user_repos(username)
analysis = analyze_all(username, repos)

generate_portfolio(username, analysis)

print(" Portfolio HTML généré : output/portfolio.html")
