import os
import smtplib
import imghdr
from email.message import EmailMessage

GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
GMAIL_ACCOUNT = os.getenv("GMAIL_ACCOUNT")


def send_email(image_path):
    email_msg = EmailMessage()
    email_msg["Subject"] = "Object Captured by Webcam"
    email_msg.set_content("Motion activated the camera program.")

    with open(image_path, "rb") as bin_file:
        content = bin_file.read()

    image_type = imghdr.what(image_path)
    email_msg.add_attachment(content, maintype="image",
                             subtype=image_type)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    print(GMAIL_ACCOUNT, GMAIL_APP_PASSWORD)
    gmail.login(GMAIL_ACCOUNT, GMAIL_APP_PASSWORD)
    gmail.sendmail(GMAIL_ACCOUNT, GMAIL_ACCOUNT, email_msg.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="test_data/1.png")
