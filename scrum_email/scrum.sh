#send_to="etosch@cs.umass.edu"
send_to="womenmembers@cs.umass.edu"
subject="HAPPENING SOON: CS Women Weekly Hack/OH/Scrum/Hangout"
send_from="CS Women Co-Chairs <womenchairs@cs.umass.edu>"
mailx -r "$send_from" -s "$subject" -Ssignature=~/cochair_resources/signature.txt "$send_to" < ~/cochair_resources/scrum_email/email_template.txt