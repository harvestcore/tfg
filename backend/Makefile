build:
	apk add build-base libffi-dev openssl-dev sshpass && pip3 install -r requirements.txt

run:
	gunicorn -b 0.0.0.0:5000 wsgi:app
