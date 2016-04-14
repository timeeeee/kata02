pep8:
	pep8 *.py

test:
	nosetests *.py

clean:
	rm -f *pyc *~
