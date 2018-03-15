import setplib
from email.mime.text import MIMEText
from email.header import Header

#發送郵箱服務器
smtpserver='smtp.sina.com'
#發送郵箱用戶/密碼
user='username@sina.com'
password='123456'
#發送郵箱
sender='username@sina.com'
#接收郵箱
receiver='receive@126.com'
#發送郵件主題
subject='Python email test'
#發送的附件
sendfile=open('D:\\testpro\\report\\log.txt','rb').read()

att=MIMEText(sendfile,'base64','utf-8')
att["Content=Type"]='applicaiton/octet-stream'
att['Content-Disposition']='attachment; filename="log.txt"'
msgRoot=MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)

#編寫HTML類型的郵件正文
msg=MIMEText('<html><hl>你好!</hl></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')


#連接發送郵件
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user.password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
