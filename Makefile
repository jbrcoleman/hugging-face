install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203 example_src/*.py


format:
	black **/*.py