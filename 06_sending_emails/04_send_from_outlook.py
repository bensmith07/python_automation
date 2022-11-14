import smtplib
import env

sender = 'some_email@outlook.com'
receiver = 'ben.f.smith07@gmail.com'

subject = 'This is the subject'

message = '''
Here is the content of the email. 
'''

server = smtplib.SMTP('smtp.office365.com', 587) # domain and port number for outlook servers
server.starttls()
server.login(sender, env.password)
server.sendmail(sender, receiver, message)
server.quit()
