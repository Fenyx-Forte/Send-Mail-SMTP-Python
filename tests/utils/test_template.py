from email.mime.text import MIMEText

from jinja2 import Template

from Send_Mail_SMTP_Python.utils import template


def test_get_content_file() -> None:
    """Test for the function get_content_file.

    This test verifies if the function is able to correctly read the content of a file.

    Args:
        None

    Returns:
        None
    """

    path_file = 'resources/test_data/test.txt'

    content_file = template.get_content_file(path_file)

    assert content_file == '123\n'


def test_get_template() -> None:
    """Test for the function get_template.

    This test verifies if the function is able to correctly get templates from files.

    Args:
        None

    Returns:
        None
    """

    file_html = 'test_email.html'
    file_txt = 'test_email.txt'

    html_content = template.get_template(file_html)
    txt_content = template.get_template(file_txt)

    assert isinstance(html_content, Template)
    assert isinstance(txt_content, Template)

    assert html_content.render(title='a', style_css='b', link='c') == 'abc'
    assert txt_content.render(link='c') == 'c'


def test_get_style_template() -> None:
    """Test case for the function get_style_template.

    This test verifies if the function is able to correctly retrieve the
    style template from the file.

    Args:
        None

    Returns:
        None
    """

    style_template = template.get_style_template()
    test_content = '<style type="text/css">\n123\n</style>'

    assert isinstance(style_template, Template)
    assert style_template.render(style_css='123') == test_content


def test_get_style() -> None:
    """Test case for the function get_style.

    This test verifies if the function is able to correctly retrieve the
    content of the style file.

    Args:
        None

    Returns:
        None
    """

    style_content = template.get_style('style.css')

    assert isinstance(style_content, str)

    assert style_content == '<style type="text/css">\n\n</style>'


def test_create_txt_body() -> None:
    """Test case for the function create_txt_body.

    This test verifies if the function is able to correctly create a text
    body from a template.

    Args:
        None

    Returns:
        None
    """

    # Creating test data
    template_content = 'This is a test template with {{ link }}'
    template = Template(template_content)

    link = 'https://example.com'
    txt_body = template.render(link=link)
    txt_body_obj = MIMEText(txt_body, 'plain')

    assert txt_body_obj.get_payload() == f'This is a test template with {link}'

    assert txt_body_obj['Content-Type'] == 'text/plain; charset="us-ascii"'


def test_create_html_body() -> None:
    """Test case for the function create_html_body.

    This test verifies if the function is able to correctly create an HTML
    body from a template.

    Args:
        None

    Returns:
        None
    """

    # Creating test data
    template_content = "<html><head><style>{{ style }}</style><title>{{ title }}</title></head><body><a href='{{ link }}'>Link</a></body></html>"
    template = Template(template_content)

    style = 'body { background-color: #f4f4f4; }'
    title = 'Test Email'
    link = 'https://example.com'
    html_body = template.render(style=style, title=title, link=link)
    html_body_obj = MIMEText(html_body, 'html')

    expected_html_body = (
        '<html><head><style>body { background-color: #f4f4f4; }</style>'
        "<title>Test Email</title></head><body><a href='https://example.com'>Link</a>"
        '</body></html>'
    )
    assert html_body_obj.get_payload() == expected_html_body
    assert html_body_obj['Content-Type'] == 'text/html; charset="us-ascii"'
