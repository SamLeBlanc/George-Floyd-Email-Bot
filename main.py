import smtplib
from methods import *

if __name__ == "__main__":
    main()

def main():
    data = readCSV('info.csv') # read in csv file with email data
    nms, emls, pws, subjs, bods, recips = subdivideData(data) # subdivide data into categories

    for x in range(len(emls)):
        time.sleep(5)
        gmail_user = emls[x] # get username
        gmail_password = pws[x] # get password

        subject = subjs[x] + '  ' + get_String_Time() # get subject
        body = bodyMaker(2, nms, x)
        print(body)
        recipients = recips[x] # get recipients

        server = create_Server(gmail_user, gmail_password) # create server for email login
        email = create_Email(gmail_user, recipients, subject, body) # create email
        send_Email(server, email, gmail_user, recipients, subject, body) # send email
        server.close()

    start_time = time.time() # establish timing to rerun program every 526 seconds
    elapsed_time = 0
    while elapsed_time < 526: # 8 mins 46 seconds = 526 seconds
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        time.sleep(10)
    main()
