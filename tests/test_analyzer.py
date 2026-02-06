from analyzer import analyze_repo


def test_analyze_repo_score():
    username = "testuser"

    repo = {
        "name": "repo1",
        "stargazers_count": 2,
        "forks_count": 1,
        "html_url": "https://github.com/testuser/repo1",
        "fork": False
    }

    # On "fake" commits et languages avec monkeypatch
    import analyzer

    analyzer.get_repo_commits = lambda u, r: [{"id": 1}, {"id": 2}, {"id": 3}]
    analyzer.get_languages = lambda u, r: {"Python": 1000, "HTML": 200}

    result = analyze_repo(username, repo)

    assert result["name"] == "repo1"
    assert result["commits"] == 3
    assert "Python" in result["languages"]

    # score = commits*2 + stars*5 + forks*3
    # = 3*2 + 2*5 + 1*3 = 6 + 10 + 3 = 19
    assert result["score"] == 19
