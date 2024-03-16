from email.mime.text import MIMEText
from unittest.mock import MagicMock, patch

import pytest

from Send_Mail_SMTP_Python.mail import mail


@pytest.fixture
def email_setup() -> mail.EmailSetup:
    """Returns an instance of `mail.EmailSetup` with test data.

    Returns:
        mail.EmailSetup: An instance of `mail.EmailSetup`
    """
    subject = 'Test Subject'
    sender = 'sender@example.com'
    receiver = 'receiver@example.com'
    txt_body = MIMEText('Test Text Body')
    html_body = MIMEText('Test HTML Body', 'html')
    attachment = None

    return mail.EmailSetup(subject, sender, receiver, txt_body, html_body, attachment)


def test_email_setup(email_setup):
    """Verify that the EmailSetup class stores the correct test data.

    This test checks if the EmailSetup object is initialized with the
    correct values for its attributes.

    Args:
        email_setup (mail.EmailSetup): The EmailSetup object to be tested.
    """
    subject = 'Test Subject'
    sender = 'sender@example.com'
    receiver = 'receiver@example.com'
    txt_body = MIMEText('Test Text Body')
    html_body = MIMEText('Test HTML Body', 'html')
    attachment = None

    assert email_setup.subject == subject
    assert email_setup.sender == sender
    assert email_setup.receiver == receiver
    assert email_setup.txt_body.as_string() == txt_body.as_string()
    assert email_setup.html_body.as_string() == html_body.as_string()
    assert email_setup.attachment == attachment


def test_create_email(email_setup):
    """
    Test the creation of an email using the `create_email` function.

    This test verifies that the `create_email` function correctly creates an
    email using the provided `email_setup` object.

    Args:
        email_setup (EmailSetup): The EmailSetup object containing the
            email's subject, sender, receiver, text body, html body, and
            attachment.

    Returns:
        None
    """
    # Set up test data
    subject = 'Test Subject'
    sender = 'sender@example.com'
    receiver = 'receiver@example.com'
    txt_body = MIMEText('Test Text Body')
    html_body = MIMEText('Test HTML Body', 'html')
    attachment = None

    # Create email using test data
    email = mail.create_email(email_setup)

    # Assert that the email's subject, sender, receiver, text body, and html body are correct
    assert email['Subject'] == subject
    assert email['From'] == sender
    assert email['To'] == receiver
    assert email.get_payload()[0].as_string() == txt_body.as_string()
    assert email.get_payload()[1].as_string() == html_body.as_string()


@patch('Send_Mail_SMTP_Python.mail.mail.create_email')
def test_send_email(mock_create_email):
    """Test the `send_email` function.

    This function tests the `send_email` function by mocking the
    `create_email` function and verifying that it correctly calls the
    `sendmail` method of the `connection` object.

    Args:
        mock_create_email (MagicMock): Mock object for the `create_email`
            function.

    Returns:
        None
    """

    # Set up mock objects
    connection = MagicMock()
    email_setup = MagicMock()

    # Mock the return value of create_email
    mock_email = MagicMock()
    mock_create_email.return_value = mock_email

    # Call the function to send the email
    mail.send_email(connection, email_setup)

    # Assertions
    mock_create_email.assert_called_once_with(email_setup)
    connection.sendmail.assert_called_once_with(
        email_setup.sender, email_setup.receiver, mock_email.as_string()
    )
