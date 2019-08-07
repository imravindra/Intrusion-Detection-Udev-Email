#!/usr/bin/python36

import cv2 as cv
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 




cap = cv.VideoCapture(0)
ret, photo = cap.read()
cv.imwrite('/root/hey.png', photo)
cap.release()

PASSWORD=''
fromaddr = ""
toaddr = ""

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Security Alert"

# string to store the body of the mail 
body = "Hey Ravi! Someone just plugged a usb device in your system! Check attachment to see intruder!"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
filename = "hey.png"
attachment = open("/root/hey.png", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, PASSWORD) 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 

