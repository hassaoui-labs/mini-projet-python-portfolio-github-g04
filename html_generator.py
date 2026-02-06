import os
from jinja2 import Environment, FileSystemLoader

def generate_html(projects, config):
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))

    template = env.get_template("portfolio.html")

    data = {
        "projects": projects,
        "config": config,
    }

    output_path = config["portfolio"]["output_path"]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template.render(**data))

    print(f"✅ Portfolio généré : {output_path}")
