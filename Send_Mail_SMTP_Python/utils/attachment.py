from email import encoders
from email.mime.base import MIMEBase


def create_attachment(filename: str) -> MIMEBase:
    # Open PDF file in binary mode
    with open(filename, "rb") as file:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(file.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(attachment)

    # Add header as key/value pair to attachment part
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    return attachment
