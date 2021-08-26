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
    if (bodNum == 1):
        body = 'Dear Seattle City Leadership,\n\n8 minutes and 46 seconds have passed, and you still have not addressed any of my concerns. My name is ' + nms[x] + ' and I am a resident of Seattle. I am writing to demand that the City Council adopt a People’s Budget that prioritizes community wellbeing and redirects funding away from the police.\n\nWe are in the midst of widespread upheaval over the systemic violence of policing, embodied by the SPD’s well documented history of murdering Black people. I will no longer accept empty gestures and suggestions of “reform.” I am demanding that my voice be heard now, and that real change be made to the way this city allocates its resources.\n\nRather than prioritize the quality of life for all of Seattle with a proportional housing and development budget, Mayor Durkan chooses to prioritize the SPD. In the 2019-2020 proposed budget, the funding for the Office of Housing, which provides grants for affordable housing, remained unchanged at only $69.1 million. In comparison, the SPD was allocated a budget of $363 million, representing a 9.7% increase in funds.\n\nThis pandemic has had severe economic consequences including high unemployment causing many people to be unable to pay rent. Prior to the pandemic, 60k people were unhoused; the evictions and economic insecurity caused by COVID-19 will bring that number even higher. Support for communities in need is necessary now, more than ever. But instead, out of all departments, the Mayor has proposed an increase in funding to the SPD. The SPD has seen a rise in overtime pay which, more often than not, is paid out to officers responsible for harassing people who are unhoused, Black, Indigenous, and people of color. This money can be spent in other ways that are proven to be more effective in improving community safety and wellness.\n\nI demand that the City Council defund the SPD. I join the calls of those across the country to defund the police. I demand a budget that adequately and effectively meets the needs of at-risk Seattleites. I demand a budget that supports community wellbeing, rather than empowers the police forces that tear them apart.\n\nAlthough City Council has avoided voting or revising Mayor Durkan’s draconian budget proposal, the document is back in your hands. It is your duty to represent your constituents. I am urging you to completely revise the Seattle budget for 2020-2021 fiscal year. You need to adopt a People’s Budget. Public opinion is with me.\n\n I will continue emailing you every 8 minutes and 46 seconds until I beleive my concerns have been adequetely addressed. Thank you for your time,\n' + nms[x] + '  ' + get_String_Time()
    if (bodNum == 2):
        body = 'Dear Seattle City Leadership,\n\n8 minutes and 46 seconds have passed, and you still have not addressed any of my concerns. My name is ' + nms[x] + ' and I am a resident of Seattle. I am writing to demand that the City Council repeal drug and prostitution loitering laws. These laws target people of color and are racstly implemented. If you care about our city and want to see it prosper, we must use our police in a responsible manner. POlice must only be used in absolutely neccesary scenarios and loitering is not harmful to anyone. Please have a conscience and repeal these laws for the good of our community. Oh yeah, and DEFUND THE POLICE NOW. I will continue emailing you every 8 minutes and 46 seconds until I beleive my concerns have been adequetely addressed. Thank you for your time,\n' + nms[x] + '  ' + get_String_Time()
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
