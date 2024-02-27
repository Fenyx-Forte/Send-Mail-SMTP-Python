from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader, Template


def get_template(filename: str) -> Template:
    env = Environment(loader=FileSystemLoader("resources/templates"))
    template = env.get_template(filename)
    return template


def get_style(filename: str) -> str:
    with open(f"resources/styles/{filename}", "r") as file:
        style = file.read()

    return style


def create_txt_body(template: Template, name: str, link: str) -> MIMEText:
    txt_body = template.render(name=name, link=link)

    return MIMEText(txt_body, "plain")


def create_html_body(template: Template, style: str, name: str, link: str) -> MIMEText:
    html_body = template.render(style=style, name=name, link=link)

    return MIMEText(html_body, "html")


def create_email_body(
    filename_template_txt: str,
    filename_template_html: str,
    filename_style,
    name: str,
    link: str,
) -> list[MIMEText]:
    template_txt = get_template(filename_template_txt)
    template_html = get_template(filename_template_html)
    style = get_style(filename_style)

    txt_body = create_txt_body(template_txt, name, link)
    html_body = create_html_body(template_html, style, name, link)

    return [txt_body, html_body]
