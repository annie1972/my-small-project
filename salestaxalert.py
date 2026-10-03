import os
import smtplib
from email.message import EmailMessage

# Pull credentials from GitHub Secrets
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


def send_alert():
  sender_email = EMAIL_USER
  # Replace with your destination email address where you want to receive the alert
  recipient_email = "5133765205@tmomail.net"

  msg = EmailMessage()
  msg["Subject"] = "Sales Tax Alert - Monthly Reminder"
  msg["From"] = sender_email
  msg["To"] = recipient_email
  msg.set_content(
      "Hello,\n\nThis is your automated monthly sales tax alert running from"
      " your GitHub repository.\n\nBest regards,\nYour Automation Bot"
  )

  try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
      smtp.login(sender_email, EMAIL_PASSWORD)
      smtp.send_message(msg)
    print("Sales tax alert email sent successfully!")
  except Exception as e:
    print(f"Failed to send email: {e}")


if __name__ == "__main__":
  send_alert()
