from email.mime.base import MIMEBase

from Send_Mail_SMTP_Python.utils import attachment


def test_create_attachment() -> None:
    """Test case for the function create_attachment.

    This test verifies if the function is able to correctly create a attachment
    from a file.

    Args:
        None

    Returns:
        None
    """
    path = 'resources/test_data/test.txt'

    attachment_obj = attachment.create_attachment(path)

    assert isinstance(
        attachment_obj, MIMEBase
    ), 'The function should return a MIMEBase object.'

    expected_disposition = f'attachment; filename= {path}'
    assert attachment_obj['Content-Disposition'] == expected_disposition
    assert attachment_obj.get_content_type() == 'application/octet-stream'
