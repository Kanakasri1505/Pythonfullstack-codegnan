'''
--->SMTP (simple mail transfer protocol)
    -this is used to send emails from server to  another server....(not mail to amil but server to server)

    note::
    
    1.SMtp SSL port (it gives errors)
    ----------
    465

    2.SMTP TLS port (use this only)
    -----------
    587

    to import---

    import smtplib(connects to server)

    EmailMessage Class
    -----------------(sender mail reciver mail text to send )

    msg['Subject']='SMTP ON Mail'
    msg['From']='Sender@mail.com'
    msg['To']='Receiver@mail.com'
##to send to one person
import smtplib
from email.message import EmailMessage
sender ='saranyasiri2005@gmail.com'
password='xhojmflindrozphg' #generate going to google manage accounts turn on twostep verification and go to app passwards and create a app passward
msg=EmailMessage() #beacuse emailmessage is a long name we assigned it to a shorter one no another use

msg['Subject']='Welcome Mail'
msg['From']=sender
msg['To']='bhavanajoseph84392@gmail.com'

msg.set_content('hi Bhavana >3 !!!!')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #to start the mail
server.login(sender,password)
server.send_message(msg)
server.quit() #to stop
'''


##to bulk mails
import smtplib
from email.message import EmailMessage
sender ='saranyasiri2005@gmail.com'
password='puldnmjciebfryiz'
receiver=['bhavanajoseph84392@gmail.com','kanakasrikssn@gmail.com','kanakasri1505@gmail.com','chandinikandregula5@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)

for mail in receiver:
    msg=EmailMessage()
    
    msg['Subject']='Welcome Mail'
    msg['From']=sender
    msg['To']=mail

    msg.set_content('hi bro!!!! \n class is fun right?')

    server.send_message(msg)
server.quit() #to stop


