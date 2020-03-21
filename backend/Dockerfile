FROM python:3.6-alpine

COPY . ./app
RUN apk update && \
    apk add make

WORKDIR ./app
EXPOSE 5000

RUN make build
CMD ["make", "run"]
