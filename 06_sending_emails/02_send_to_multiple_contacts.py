import yagmail
import env
import time
from datetime import datetime as dt
import pandas as pd

sender = 'ben.f.smith07@gmail.com'



yag = yagmail.SMTP(user=sender, password=env.PASSWORD)

df = pd.read_csv('contacts.csv')

for idx, row in df.iterrows():

    receiver_name = row['name']
    receiver_email = row['email']


    subject = f'{receiver_name.upper()}: This is the subject'

    contents = f'''
    Dear {receiver_name},
    Here is the content of the email. 
    '''

    yag.send(to=receiver_email, subject=subject, contents=contents)

