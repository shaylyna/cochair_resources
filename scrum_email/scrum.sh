#send_to="strubell@cs.umass.edu, etosch@cs.umass.edu, jfoley@cs.umass.edu"
send_to="womenmembers@cs.umass.edu"
subject="HAPPENING SOON: CS Women Weekly Hack/OH/Scrum/Hangout"
send_from="CS Women Co-Chairs <womenchairs@cs.umass.edu>"
mailx -r "$send_from" -s "$subject" -Ssignature=../signature.txt "$send_to" < email_template.txt