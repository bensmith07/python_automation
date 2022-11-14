import yagmail
import env
import time
from datetime import datetime as dt

sender = 'ben.f.smith07@gmail.com'
receiver = 'aexoqoajhrboow@dropmail.me'

subject = 'This is the subject'

contents = '''
Here is the content of the email. 
'''

yag = yagmail.SMTP(user=sender, password=env.PASSWORD)

while True:
    if dt.now().hour == 10 and dt.now().minute == 22:
        yag.send(to=receiver, subject=subject, contents=contents)
        time.sleep(60)
