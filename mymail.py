#!/usr/bin/python36


import smtplib 

SENDER_EMAIL=''
RECIEVER_EMAIL=''
PASSWORD=''

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(SENDER_EMAIL, PASSWORD) 

# message to be sent
message = "Hey Ravi! Someone just plugged a usb device in your system!"

# sending the mail 
s.sendmail(SENDER_EMAIL, RECIEVER_EMAIL, message) 

# terminating the session 
s.quit() 

