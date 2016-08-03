apt-get-install:
	sudo apt-get install -y python-pip python-dev build-essential openjdk-8-jre nodejs-legacy npm

node-install:
	cd frontend && npm install

venv:
	virtualenv -p /usr/bin/python3 venv

requirements:
	venv/bin/python3 venv/bin/pip3 install -r requirements.txt
	venv/bin/python3 venv/bin/pip3 install -r requirements-test.txt

install: apt-get-install node-install venv requirements

test:
	venv/bin/python3 manage.py test

run-server:
	venv/bin/python3 manage.py runserver

pycoverage:
	venv/bin/coverage erase
	venv/bin/coverage run --branch manage.py test
	venv/bin/coverage html -d coverage --omit='vehicles/tests/*','vehicles/migrations/*','venv/*','manage.py'

clean:
	rm -rf venv
	rm -rf htmlcov
	rm .coverage

setup: build-venv apply-migration load-fixtures create-superuser
	echo "all set!"
