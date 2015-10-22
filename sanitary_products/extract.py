from pyquery import PyQuery as pq
from lxml import etree
import urllib
import smtplib
import sys
from email.mime.text import MIMEText

d = pq(filename="faculty-directory")
p = d(".field-name-title > div > div")
names = [div.text for div in p]

p = d(".field-name-field-email > div > div > a")
emails = [div.text for div in p]

with open('./last_index', 'r') as f:
    last_index = int(''.join(f.readlines()).strip())
    next_index = (last_index + 1) % len(emails)

next_prof = names[next_index].split(',')[0]
last_prof = names[last_index].split(',')[0]
email_from = 'womenchairs@cs.umass.edu'
email_to = [emails[next_index]] #['strubell@cs.umass.edu', 'etosch@cs.umass.edu']

with open('../signature.txt') as f:
    signature = ''.join(f.readlines())

with open('./email_template.txt') as f:
    template = ''.join(f.readlines())

email_body = template % (next_prof, last_prof, signature)
msg = MIMEText(email_body)
msg['Subject'] = 'Test email script -- please respond with comments'
msg['From'] = email_from
msg['To'] = ', '.join(email_to)

ans = None
while not ans:
    print 'Preview Email? (Y/N)'
    ans = sys.stdin.readline().strip()
    if (ans == 'Y' or ans == 'y'):
        print email_body
    elif (ans == 'N' or ans == 'n'):
        ans = True
    else:
        ans = False
        
ans = None
while not ans:
    print 'Send Email to %s? (Y/N)' % email_to
    ans = sys.stdin.readline().strip()
    if (ans == 'Y' or ans == 'y'):
        s = smtplib.SMTP('cs.umass.edu')
        s.sendmail(email_from, email_to, msg.as_string())
        s.quit()
        with open('./last_index', 'w') as f:
            f.write(str(next_index))
    elif (ans == 'N' or ans == 'n'):
        ans = True
    else:
        ans = False
        
