from unittest.mock import Mock, patch

import pytest

from Send_Mail_SMTP_Python.mail import m_connection


@pytest.fixture
def connection_setup() -> m_connection.ConnectionSetup:
    """Fixture for creating a ConnectionSetup object.

    Returns:
        m_connection.ConnectionSetup: The ConnectionSetup object.

    """
    return m_connection.ConnectionSetup(
        server='test_server', port=1234, login='test_login', password='test_password'
    )


def test_connection_setup(connection_setup):
    """
    Test the ConnectionSetup class.

    Args:
        connection_setup (ConnectionSetup): The object to be tested.
    """

    assert connection_setup.server == 'test_server'
    assert connection_setup.port == 1234
    assert connection_setup.login == 'test_login'
    assert connection_setup.password == 'test_password'


@patch('Send_Mail_SMTP_Python.mail.m_connection.create_smtp_connection')
def test_smtpconnection_context_manager(mock_create_smtp_connection, connection_setup):
    """Test that SMTPConnection context manager creates and closes the SMTP connection.

    This function tests that when used as a context manager,
    SMTPConnection creates the SMTP connection and closes it
    when the context is exited.

    Args:
        mock_create_smtp_connection (MagicMock): Mock object representing
            create_smtp_connection.
        connection_setup (ConnectionSetup): The ConnectionSetup object.

    Returns:
        None
    """
    mock_connection = Mock()
    mock_create_smtp_connection.return_value = mock_connection

    with m_connection.SMTPConnection(connection_setup):
        pass

    mock_create_smtp_connection.assert_called_once_with(connection_setup)
    mock_connection.close.assert_called_once()


@patch('Send_Mail_SMTP_Python.mail.m_connection.ssl.create_default_context')
@patch('Send_Mail_SMTP_Python.mail.m_connection.smtplib.SMTP')
def test_create_smtp_connection(
    mock_smtp, mock_create_default_context, connection_setup
):
    """Test function to test the creation of an SMTP connection.

    This function tests if the function `create_smtp_connection`
    creates an SMTP connection using the provided `ConnectionSetup` object.

    Args:
        mock_smtp (MagicMock): Mock object representing the SMTP class.
        mock_create_default_context (MagicMock): Mock object representing the
            create_default_context function.
        connection_setup (ConnectionSetup): The ConnectionSetup object.

    Returns:
        None
    """
    mock_context = Mock()
    mock_create_default_context.return_value = mock_context

    mock_connection = mock_smtp.return_value
    m_connection.create_smtp_connection(connection_setup)

    mock_create_default_context.assert_called_once()
    mock_smtp.assert_called_once_with('test_server', 1234)
    mock_connection.starttls.assert_called_once_with(context=mock_context)
    mock_connection.login.assert_called_once_with('test_login', 'test_password')
