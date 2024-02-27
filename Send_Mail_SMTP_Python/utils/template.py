from email.mime.text import MIMEText

from jinja2 import Template


def get_content_file(path_file: str) -> str:
    with open(path_file, "r") as file:
        content = file.read()

    return content


def get_template(filename: str) -> Template:
    content = get_content_file(f"resources/templates/{filename}")
    template = Template(content)
    return template


def get_style_template() -> Template:
    content = get_content_file("resources/styles/template_style.txt")
    template = Template(content)
    return template


def get_style(filename: str) -> str:
    template = get_style_template()
    style_content = get_content_file(f"resources/styles/{filename}")
    style = template.render(style_css=style_content)

    return style


def create_txt_body(template: Template, link: str) -> MIMEText:
    txt_body = template.render(link=link)

    return MIMEText(txt_body, "plain")


def create_html_body(template: Template, style: str, title: str, link: str) -> MIMEText:
    html_body = template.render(style=style, title=title, link=link)

    return MIMEText(html_body, "html")


def create_email_body(
    filename_template_txt: str,
    filename_template_html: str,
    filename_style,
    title: str,
    link: str,
) -> list[MIMEText]:
    template_txt = get_template(filename_template_txt)
    template_html = get_template(filename_template_html)
    style = get_style(filename_style)

    txt_body = create_txt_body(template_txt, link)
    html_body = create_html_body(template_html, style, title, link)

    return [txt_body, html_body]
