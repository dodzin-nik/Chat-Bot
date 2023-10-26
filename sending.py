import smtplib, ssl

port = 587  
smtp_server = "smtp.gmail.com" #плейсхолдер
sender_email = "sender@gmail.com" #плейсхолдер
receiver_email = "reciver@gmail.com" #плейсхолдер
password = "password" #плейсхолдер

def sendtomail(mail: str):
    message = mail
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)