import smtplib
from email.mime.text import MIMEText
import getpass


def sendMail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print("[+] Connecting To Mail Server.")
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except:
        print("[-] Sending Mail Failed.")

if __name__ == '__main__':
    user = 'fcfmimage@gmail.com'
    pwd = getpass.getpass("Password")
    sendMail(user, pwd, 'edyjralvarado.ea@gmail.com',
             'Re: Important', 'Test Message')

