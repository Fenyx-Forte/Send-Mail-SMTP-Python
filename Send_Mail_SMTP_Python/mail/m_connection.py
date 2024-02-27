import smtplib
import ssl


class ConectionSetup:
    def __init__(self, server: str, port: int, login: str, password: str) -> None:
        self.server = server
        self.port = port
        self.login = login
        self.password = password


def create_smtp_connection(connection_setup: ConectionSetup) -> smtplib.SMTP:
    context_ssl = ssl.create_default_context()

    connection = smtplib.SMTP(connection_setup.server, connection_setup.port)

    connection.starttls(context=context_ssl)

    connection.login(connection_setup.login, connection_setup.password)

    return connection
