GUNICORN_PORT := $(if $(BACKEND_GUNICORN_PORT),$(BACKEND_GUNICORN_PORT),5000)
GUNICORN_PARAMS := $(BACKEND_GUNICORN_PARAMS)

build:
	apk add build-base libffi-dev openssl-dev sshpass && pip3 install -r requirements.txt

run:
	gunicorn -b 0.0.0.0:${GUNICORN_PORT} wsgi:app ${GUNICORN_PARAMS}
