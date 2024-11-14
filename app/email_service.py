import os

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_SENDER_ADDRESS = os.getenv("SENDGRID_SENDER_ADDRESS")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

def send_email(sender_address, recipient_address, subject, html_content):
    """
    Sends an email to the given recipient address.

    Params:
        sender_address (str): The email address of the sender.
        recipient_address (str): The email address of the recipient.
        subject (str): The subject of the email.
        html_content (str): The HTML content of the email.
    """
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    message = Mail(from_email=sender_address, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)
        print("Email sent successfully! Status code:", response.status_code)
    except Exception as err:
        print(f"Error sending email: {err}")

if __name__ == "__main__":
    send_email(
        sender_address=SENDGRID_SENDER_ADDRESS,
        recipient_address="sjolly03@gmail.com",
        subject="Test",
        html_content="<p>This is a test.</p>"
    )