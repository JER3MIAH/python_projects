import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Owoade Jeremiah'
email['to'] = 'jeremiahbrownie@gmail.com'
email['subject'] = 'You have won a 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jeremiahkenneth0@gmail.com', 'ijintorplqhwgltg')
    smtp.send_message(email)
    print('Sent!')
