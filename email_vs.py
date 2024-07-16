import streamlit as st

st.title("🎈 My new app")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



import os
import json
config_file = st.file_uploader("Choose a file")
config = json.load(config_file)
#with open('config.json') as config_file:
   

# Access the credentials
#sender_email  = config['email_user']
#password  = config['email_pass']
recipients = [
    "deepanshugoyal509@gmail.com"
]
sender_email = config['email_user']
subject = "Subject of the Email"
body = """
Hello,

This is a test email sent from Python script.

Best regards,
Deepanshu Goyal
"""
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
def send_email(recipient_email,sender_email,config,subject,body,attachment_path=None):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = config['email_user']
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
       # Add an attachment if provided

        if attachment_path:
            filename = os.path.basename(attachment_path)
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={filename}',
                )
                msg.attach(part)
                
        # Connect to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(config['email_user'], config['email_pass'])

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        print(f"Email successfully sent to {recipient_email}")
        
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

attachment_path = r"E:\Workoopolis pdf &excel\PythonProject-3  Projects  using Python.docx"

for recipient in recipients:
    send_email(recipient,sender_email,config,subject,body,attachment_path)
