import logging
import smtplib
import ssl

from Send_Mail_SMTP_Python.my_log import my_log

module_name = __name__.split('.')[-1]

logger = logging.getLogger(module_name)


class ConnectionSetup:
    """This class stores the necessary properties to establish an
    smtp connection.
    """

    @my_log.debug_log(logger)
    def __init__(self, server: str, port: int, login: str, password: str) -> None:
        """Initialize a new instance.

        Args:
            server (str): server name
            port (int): server port
            login (str): user login
            password (str): user password
        """

        self.server = server
        self.port = port
        self.login = login
        self.password = password


class SMTPConnection:
    """This class serves as a context manager for SMTP connections."""

    @my_log.debug_log(logger)
    def __init__(self, connection_setup: ConnectionSetup) -> None:
        """Initialize a new instance.

        Args:
            connection_setup (ConnectionSetup): connection setup
        """

        self.setup = connection_setup
        self.connection = None

    @my_log.debug_log(logger)
    def __enter__(self) -> smtplib.SMTP:
        """Create a smtp connection instance

        Returns:
            smtplib.SMTP: smtp connection
        """

        logger.info('Connecting to smtp server...')

        self.connection = create_smtp_connection(self.setup)

        logger.info('Connection established!')

        return self.connection

    @my_log.debug_log(logger)
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Close the smtp connection instance

        Args:
            exc_type (_type_): exception type
            exc_val (_type_): exception value
            exc_tb (_type_): exception traceback
        """

        logger.info('Closing connection...')
        self.connection.close()
        logger.info('Connection closed!')


@my_log.debug_log(logger)
def create_smtp_connection(connection_setup: ConnectionSetup) -> smtplib.SMTP:
    """Create a smtp connection instance

    Args:
        connection_setup (ConnectionSetup): connection setup

    Returns:
        smtplib.SMTP: smtp connection instance
    """
    context_ssl = ssl.create_default_context()

    connection = smtplib.SMTP(connection_setup.server, connection_setup.port)

    connection.starttls(context=context_ssl)

    connection.login(connection_setup.login, connection_setup.password)

    return connection
