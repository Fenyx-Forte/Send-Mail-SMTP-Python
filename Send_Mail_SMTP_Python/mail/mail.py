import smtplib
import ssl


def send_mail() -> None:
    server = "smtp.gmail.com"
    port = 587
    context_ssl = ssl.create_default_context()

    with smtplib.SMTP(server, port) as server:
        server.starttls(context=context_ssl)
        ...
