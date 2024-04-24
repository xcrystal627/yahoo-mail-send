import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from dotenv import dotenv_values
 

def send_mail(product_link):
    print(f'trying to send mail')

    env_values = dotenv_values('.env')

    pwd = env_values['EMAIL_PASSWORD']
    msg = EmailMessage()
    msg['From'] = env_values['EMAIL_ADDRESS']
    msg['To'] = env_values['RECEIVER_EMAIL']
    msg['Subject'] = f"商品を注文しました。" 
    
    mail_text = f"商品{product_link}を注文しました。" 
    
    try:
        server = smtplib.SMTP_SSL(host=env_values['EMAIL_HOST'], port=env_values['EMAIL_PORT'], timeout=60)
        server.ehlo()
        print('before ttls')
        # server.starttls()
        print('after ttls')
        server.login(msg['From'], pwd)

        print('after login')
        msg.set_content(mail_text)
        server.send_message(msg)
        print(f'Mail was send to {msg["To"]}')
        server.quit()

    except Exception as error:
        print(error)


send_mail('test')