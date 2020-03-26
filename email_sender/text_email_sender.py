import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'John'
email['to'] = 'john@gmail.com'
email['subject'] = 'message from the dark side'
email.set_content('I am a python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('john@gmail.com', 'qwertyuiop')
    smtp.send_message(email)
    print('all good!')
