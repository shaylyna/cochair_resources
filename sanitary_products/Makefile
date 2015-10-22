.PHONY := pyquery-install

faculty-directory:
	wget https://www.cics.umass.edu/faculty/faculty-directory

pyquery-install:
	pip install pyquery

extracted.tsv: faculty-directory pyquery-install
	python extract.py
