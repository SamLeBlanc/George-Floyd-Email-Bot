import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import time
from datetime import datetime

import csv

def create_Server(user, password):
    print(user)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # settings for Gmails SMTP service
        server.ehlo() # idk what this does
        server.login(user, password) # login to Gmail using SMTP
        print ('Log in successful!')
        return server
    except:
        print ('Could not log in...')

def create_Email(frum, tos, sub, bod):
    msg = MIMEMultipart() # instance of MIMEMultipart
    msg['From'] = frum # storing the senders email address
    msg['To'] = ', '.join(tos) # storing the receivers email addresses
    msg['Subject'] = sub # storing the subject
    body = bod # string to store the body of the mail
    msg.attach(MIMEText(body, 'plain')) # attach the body with the msg instance
    text = msg.as_string() # Converts the Multipart msg into a string
    return text

def send_Email(serv, email, frum, tos, sub, bod):
    try:
        serv.sendmail(frum, tos, email) # send email
        print ('Email sent!') # print email info
        print ('From: ' + frum)
        print ('To: ' + ', '.join(tos))
        print ('Subject: ' + sub)
        print ('Body: ' + bod)
    except:
        print ('Email did not send...')

def get_String_Time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return str(current_time)

def readCSV(fil): # read email data from csv file
    data = [];
    with open(fil) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
             data.append(row)
    return data

def bodyMaker(bodNum, nms, x):
    body=''
    if (bodNum == 1): body = 'this is body 1'
    if (bodNum == 2): body = 'this is body 2'
    return body

def subdivideData(d): # subdivide data into categories (names, emails, passwords, subjects, bodies, recipients)
    nm = [];
    em = [];
    pw = [];
    sb = [];
    bd = [];
    rcp = [];

    for x in range (len(d)):
        nm.append(d[x][0])
        em.append(d[x][1])
        pw.append(d[x][2])
        sb.append(d[x][3])
        bd.append(d[x][4])

        r = [];
        y = 5;
        while y < len(d[x]):
            r.append(d[x][y])
            y = y+1
        rcp.append(r)
    return nm, em, pw, sb, bd, rcp
