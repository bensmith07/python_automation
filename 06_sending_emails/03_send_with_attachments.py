import yagmail
import env
import time
from datetime import datetime as dt

sender = 'ben.f.smith07@gmail.com'
receiver = 'ben.f.smith07@gmail.com'

subject = 'This is the subject'

body = '''
Here is the content of the email. 
'''

attachment = 'contacts.csv'

contents = [body, attachment]

yag = yagmail.SMTP(user=sender, password=env.PASSWORD)

yag.send(to=receiver, subject=subject, contents=contents)
