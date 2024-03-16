from email.mime.image import MIMEImage

from Send_Mail_SMTP_Python.utils import images


def test_embedded_image():
    """Test case for the function embedded_image.

    This test verifies if the function is able to correctly create a MIMEImage
    object for embedding an image in an email.

    Args:
        None

    Returns:
        None
    """

    filename = 'example.jpg'

    embedded_image = images.embedded_image(filename)

    assert isinstance(
        embedded_image, MIMEImage
    ), 'The function should return a MIMEImage object.'

    assert (
        embedded_image['Content-Disposition'] == f'inline; filename={filename}'
    ), "The function should set the 'Content-Disposition' header correctly."
