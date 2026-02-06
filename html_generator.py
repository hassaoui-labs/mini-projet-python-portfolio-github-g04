import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate_portfolio(username, data):
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(["html", "xml"])
    )

    template = env.get_template("portfolio.html")

    html_content = template.render(
        username=username,
        repos=data
    )

    os.makedirs("output", exist_ok=True)

    with open("output/portfolio.html", "w", encoding="utf-8") as f:
        f.write(html_content)
