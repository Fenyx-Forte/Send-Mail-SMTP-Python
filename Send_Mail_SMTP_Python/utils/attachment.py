import logging
from email import encoders
from email.mime.base import MIMEBase
from pathlib import Path

from Send_Mail_SMTP_Python.my_log import my_log

module_name = __name__.split('.')[-1]

logger = logging.getLogger(module_name)


# Accepts:
# - images
# - documents
# - any binary data
@my_log.debug_log(logger)
def create_attachment(filename: str) -> MIMEBase:
    """This function receives a file and returns an object that can be attached
    to an email.

    Args:
        filename (str): filename (images, documents, binary data)

    Returns:
        MIMEBase: attachment
    """

    path = Path(filename).resolve()

    # Open PDF file in binary mode
    with open(path, 'rb') as file:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(file.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(attachment)

    # Add header as key/value pair to attachment part
    attachment.add_header(
        'Content-Disposition',
        f'attachment; filename= {filename}',
    )

    logger.info('Attachment created!')
    return attachment
