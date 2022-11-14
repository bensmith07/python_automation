import yagmail
import env
import time

sender = 'ben.f.smith07@gmail.com'
receiver = 'aexoqoajhrboow@dropmail.me'

subject = 'This is the subject'

contents = '''
Here is the content of the email. 
'''

yag = yagmail.SMTP(user=sender, password=env.PASSWORD)

for i in range(10):
    yag.send(to=receiver, subject=subject, contents=contents)
    time.sleep(10)