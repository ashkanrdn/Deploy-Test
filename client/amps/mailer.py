import smtplib
import time 

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'fabsshop001@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'FABSSH0P'  #change this to match your gmail password

class Emailer():
    def sendmail(self, recipients, subject, content):
         
        for recipient in recipients:
        #Create Headers
            headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
            headers = "\r\n".join(headers)
    
            #Connect to Gmail Server
            session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            session.ehlo()
            session.starttls()
            session.ehlo()
    
            #Login to Gmail
            session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    
            #Send Email & Exit
            session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
            session.quit
            print('sent email to ', recipient)
            # time.sleep(5)
 
# sender = Emailer()

# ###Defining variables to test the emailer class
# sendTo = 'matt.gindlesparger@gmail.com'
# emailSubject = "Hello World 2"
# emailContent = "This is a test of my Emailer Class from the raspberry pi. please reply if you receive this email."
 
# #Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
# sender.sendmail(sendTo, emailSubject, emailContent)


