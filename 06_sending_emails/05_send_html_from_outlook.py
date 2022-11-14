import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBASE
from email import encoders
import env

sender = 'some_email@outlook.com'
receiver = 'ben.f.smith07@gmail.com'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello'

body = '''
        <h1> Hi there! </h1>
        <h2> Text 1 </h2>
        <h3> Text 2 </h3>
        <p> The quick brown fox jumped over the lazy red dog. </p>
    '''
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

attachment_path = 'contacts.csv'
attachment = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
message.attacah(payload)


server = smtplib.SMTP('smtp.office365.com', 587) # domain and port number for outlook servers
server.starttls()
server.login(sender, env.password)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()
