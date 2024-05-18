import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    #server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('yaddanapudisahithi04@gmail.com','rymu dyif xbns hsic')
    msg=EmailMessage()
    msg['FROM']='yaddanapudisahithi04@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()