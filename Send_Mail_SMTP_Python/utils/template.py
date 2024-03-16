import logging
from email.mime.text import MIMEText
from pathlib import Path

from jinja2 import Template

from Send_Mail_SMTP_Python.my_log import my_log

module_name = __name__.split('.')[-1]

logger = logging.getLogger(module_name)


@my_log.debug_log(logger)
def get_content_file(path_file: str) -> str:
    """This function returns the content of a file

    Args:
        path_file (str): relative path

    Returns:
        str: file content
    """

    path = Path(path_file).resolve()
    with open(path, 'r') as file:
        content = file.read()

    return content


@my_log.debug_log(logger)
def get_template(filename: str) -> Template:
    """This function returns a file as a jinja2 template

    Args:
        filename (str): filename

    Returns:
        Template: jinja2 template object
    """

    content = get_content_file(f'resources/templates/{filename}')
    template = Template(content)
    return template


@my_log.debug_log(logger)
def get_style_template() -> Template:
    """This function returns the "template_style.txt" as a jinja2 template.

    Returns:
        Template: jinja2 template object
    """

    content = get_content_file('resources/styles/template_style.txt')
    template = Template(content)
    return template


@my_log.debug_log(logger)
def get_style(filename: str) -> str:
    """This function returns a css template to insert in a html template.

    Args:
        filename (str): css filename

    Returns:
        str: css content
    """

    template = get_style_template()
    style_content = get_content_file(f'resources/styles/{filename}')
    style = template.render(style_css=style_content)

    return style


@my_log.debug_log(logger)
def create_txt_body(template: Template, link: str) -> MIMEText:
    """This function create a txt body for email.

    Args:
        template (Template): jinja2 template
        link (str): link to insert in template

    Returns:
        MIMEText: txt body
    """

    txt_body = template.render(link=link)

    return MIMEText(txt_body, 'plain')


@my_log.debug_log(logger)
def create_html_body(template: Template, style: str, title: str, link: str) -> MIMEText:
    """This function create a html body for email.

    Args:
        template (Template): jinja2 template
        style (str): style to insert in template
        title (str): title to insert in template
        link (str): link to insert in template

    Returns:
        MIMEText: html body
    """

    html_body = template.render(style=style, title=title, link=link)

    return MIMEText(html_body, 'html')


@my_log.debug_log(logger)
def create_email_body(
    filename_template_txt: str,
    filename_template_html: str,
    filename_style,
    title: str,
    link: str,
) -> list[MIMEText]:
    """This function create a complete email body

    Args:
        filename_template_txt (str): txt template filename
        filename_template_html (str): html template filename
        filename_style (_type_): style to insert in template
        title (str): title to insert in template
        link (str): link to insert in template

    Returns:
        list[MIMEText]: email body
    """

    template_txt = get_template(filename_template_txt)
    template_html = get_template(filename_template_html)
    style = get_style(filename_style)

    txt_body = create_txt_body(template_txt, link)
    html_body = create_html_body(template_html, style, title, link)

    logger.info('Email body created successfully!')
    return [txt_body, html_body]
