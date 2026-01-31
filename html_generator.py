from jinja2 import Environment, FileSystemLoader

def generate_portfolio(username, data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("portfolio.html")

    html_content = template.render(
        username=username,
        repos=data
    )

    with open("output/portfolio.html", "w", encoding="utf-8") as f:
        f.write(html_content)
