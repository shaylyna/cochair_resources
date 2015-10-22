# Instructions to generate the email.

```
python extract.py
```

The Makefile updates the list of faculty. Since the structure of the website may change, be mindful that this script may break. To get the list of faculty members (execute at your own risk!): `wget https://www.cics.umass.edu/faculty/faculty-directory`

NOTE: After sending the email, you MUST commit and push the changes this script made to the repo. It tracks the index of the last faculty member who sponsored the initiative, so if you do not update the index, the next person will send an email to the same person whom we had previously asked!

# Requirements

* wget
* pip
* pyquery
* sendmail
