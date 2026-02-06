import debugpy
from github_api import get_user_repos
from analyzer import analyze_all
from html_generator import generate_portfolio


def main():
    username = input("GitHub username: ").strip()

    repos = get_user_repos(username)
    analysis = analyze_all(username, repos)

    generate_portfolio(username, analysis)

    print("Portfolio HTML généré : output/portfolio.html")


if __name__ == "__main__":
    # Active debugpy seulement si tu veux debug
    # Lance ensuite: python main.py
    debug_mode = False

    if debug_mode:
        debugpy.listen(("0.0.0.0", 5678))
        print("⏳ Waiting for debugger attach on port 5678...")
        debugpy.wait_for_client()
        print("✅ Debugger attached!")

    main()
