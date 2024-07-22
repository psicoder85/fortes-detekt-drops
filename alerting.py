import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(subject, body, to_email):
    """
    Send an email alert.
    
    Args:
        subject (str): Subject of the email.
        body (str): Body of the email.
        to_email (str): Recipient email address.

    Returns:
        None
    """
    from_email = "your_email@example.com"
    from_password = "your_email_password"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email alert sent successfully")
    except Exception as e:
        print(f"Failed to send email alert: {e}")
