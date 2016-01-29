# Note: cannot run this on balder because we don't have the python depdencies and
# don't have the permissions to install. 

from email.mime.text import MIMEText

email_from = 'womenchairs@cs.umass.edu'
# email_to = ['womenmembers@cs.umass.edu']
email_to = ['strubell@cs.umass.edu', 'etosch@cs.umass.edu', 'jfoley@cs.umass.edu']

with open('../signature.txt') as f:
    signature = ''.join(f.readlines())

with open('./email_template.txt') as f:
    template = ''.join(f.readlines())

email_body = template % signature
msg = MIMEText(email_body)
msg['Subject'] = 'HAPPENING SOON: CS Women Weekly Hack/OH/Scrum/Hangout'
msg['From'] = email_from
msg['To'] = ', '.join(email_to)
msg['CC'] = email_from

s = smtplib.SMTP('cs.umass.edu')
s.sendmail(email_from, email_to, msg.as_string())
s.quit()
