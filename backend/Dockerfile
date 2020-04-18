FROM python:3.6-alpine

COPY ./config ./app/config
COPY ./src ./app/src
COPY ./wsgi.py ./app
COPY ./Makefile ./app
COPY ./requirements.txt ./app
COPY ./LICENSE ./app

RUN apk update && \
    apk add make

WORKDIR ./app
EXPOSE 5000

RUN make build
CMD ["make", "run"]
