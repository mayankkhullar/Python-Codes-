import smtplib
from smtplib import SMTPException
sender = "mayank.khullar@amdocs.com"
receivers = ['mayank.khullar@t-mobile.com']
message = "DDDDD"

try :
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender , receivers , message)
    print 'sent'
except SMTPException:
    print 'Error'

print smtpObj.ehlo()
