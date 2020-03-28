test:
	py.test

coverage:
	py.test --cov=.
	coverage html
	sensible-browser htmlcov/index.html