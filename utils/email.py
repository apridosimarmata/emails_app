import smtplib

def send_email(to, subject, message):
    gmail_user = "your_gmail_username"
    gmail_password = "your_gmail_password"
    
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        message = f"Subject: {subject}\n\n{message}"
        server.sendmail(gmail_user, to, message)
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email: ", e)
    finally:
        server.quit()