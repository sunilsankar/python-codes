#!/usr/bin/python
#Author Sunil Sankar
#Date 15-Oct-2017
#Example of sending email using gmail with attachment
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = ""
toaddr = ""
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "sending mail from python script"
 
body = "python script"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "lab1.txt"
attachment = open("d:/Lab1.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.close()
print('successfully sent the mail')
