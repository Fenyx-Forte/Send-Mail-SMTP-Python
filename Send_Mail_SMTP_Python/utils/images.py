import logging
from email.mime.image import MIMEImage

from Send_Mail_SMTP_Python.my_log import my_log

module_name = __name__.split('.')[-1]

logger = logging.getLogger(module_name)


# To reference the image in email body, use:
# <img src="cid:filename">
@my_log.debug_log(logger)
def embedded_image(filename: str) -> MIMEImage:
    """This function receives a image filename and returns an image that can be used in email body.
    Obs:
        To reference the image in email body, use:
        <img src="cid:filename">

    Args:
        filename (str): image filename

    Returns:
        MIMEImage: embedded image
    """
    with open(f'resources/images/{filename}', 'rb') as file:
        image = MIMEImage(file.read())

    image.add_header('Content-Disposition', f'inline; filename={filename}')

    logger.info('Embedded image created!')
    return image
