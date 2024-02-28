import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSetup:
    """This class stores the necessary properties of an email."""

    def __init__(
        self,
        subject: str,
        sender: str,
        receiver: str,
        txt_body: MIMEText,
        html_body: MIMEText,
        attachment: MIMEBase = None,
    ):
        """Initialize a new instance.

        Args:
            subject (str): _description_
            sender (str): _description_
            receiver (str): _description_
            txt_body (MIMEText): _description_
            html_body (MIMEText): _description_
            attachment (MIMEBase, optional): _description_. Defaults to None.
        """

        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.txt_body = txt_body
        self.html_body = html_body
        self.attachment = attachment


def create_email(email_setup: EmailSetup) -> MIMEMultipart:
    """This function creates an instance of an email

    Args:
        email_setup (EmailSetup): necessary properties of an email

    Returns:
        MIMEMultipart: instance of an email
    """

    email = MIMEMultipart("alternative")

    email["Subject"] = email_setup.subject
    email["From"] = email_setup.sender
    email["To"] = email_setup.receiver

    email.attach(email_setup.txt_body)
    email.attach(email_setup.html_body)

    if email_setup.attachment:
        email.attach(email_setup.attachment)

    return email


def send_email(connection: smtplib.SMTP, email_setup: EmailSetup) -> None:
    """This function use a smtp connection and a email setup to create and send
    an email

    Args:
        connection (smtplib.SMTP): smtp connection
        email_setup (EmailSetup): necessary properties of an email
    """

    email = create_email(email_setup)

    message = email.as_string()

    connection.sendmail(email_setup.sender, email_setup.receiver, message)

    print("Email sent successfully!/n")
