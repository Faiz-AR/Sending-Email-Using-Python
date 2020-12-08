import smtplib
import getpass

def emailLogin():
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = getpass.getpass("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    smtp_object.login(email, password)
    return smtp_object, email

def sendEmail(smtp_object,email):
    to_address = getpass.getpass("Enter the email of the recipient: ")
    subject = input("Enter the subject line: ")
    message = input("Type out the message you want to send: ")
    msg = "Subject: " + subject + '\n' + message
    smtp_object.sendmail(email,to_address,msg)
    print('Mail successfully sent!')
    smtp_object.quit()

def main():
    obj, user_email = emailLogin()
    sendEmail(obj,user_email)

main()