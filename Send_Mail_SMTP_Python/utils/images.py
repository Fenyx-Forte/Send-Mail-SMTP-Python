from email.mime.image import MIMEImage


# To reference the image in email body, use:
# <img src="cid:filename">
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
    with open(f"resources/images/{filename}", "rb") as file:
        image = MIMEImage(file.read())

    image.add_header("Content-Disposition", f"inline; filename={filename}")

    return image
