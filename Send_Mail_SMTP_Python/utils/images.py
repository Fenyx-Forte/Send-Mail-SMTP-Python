from email.mime.image import MIMEImage


# To reference the image in email body, use:
# <img src="cid:filename">
def embedded_image(filename: str) -> MIMEImage:
    with open(f"resources/images/{filename}", "rb") as file:
        image = MIMEImage(file.read())

    image.add_header("Content-Disposition", f"inline; filename={filename}")

    return image
