import logging

from Send_Mail_SMTP_Python.mail import m_connection, mail
from Send_Mail_SMTP_Python.my_log import my_log
from Send_Mail_SMTP_Python.utils import env_vars, template

module_name = __name__.split('.')[-1]

logger = logging.getLogger(module_name)


def main() -> None:
    logger.info('Starting...')

    # Connection setup
    server = 'smtp.gmail.com'
    port = 587
    login = env_vars.LOGIN
    password = env_vars.PASSWORD

    connection_setup = m_connection.ConnectionSetup(server, port, login, password)

    # Email body setup
    title = 'Fenyx Forte - Analista de Dados Jr'
    link = 'https://fenyx-forte.github.io/'

    filename_template_txt = 'email.txt'
    filename_template_html = 'email.html'
    filename_style = 'style.css'

    list_email_body = template.create_email_body(
        filename_template_txt, filename_template_html, filename_style, title, link
    )

    txt_body = list_email_body[0]
    html_body = list_email_body[1]

    # Email setup
    subject = title
    sender_email = env_vars.SENDER_EMAIL
    receiver_email = env_vars.RECEIVER_EMAIL
    attachment = None

    email_setup = mail.EmailSetup(
        subject, sender_email, receiver_email, txt_body, html_body, attachment
    )

    # Send email
    with m_connection.SMTPConnection(connection_setup) as connection:
        mail.send_email(connection, email_setup)

    logger.info('End')
