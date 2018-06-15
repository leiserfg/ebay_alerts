FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apk add --update --no-cache gcc libxslt-dev libc-dev py3-urllib3 #lxml needs this
COPY requirements.txt requirements.txt

# -- Install dependencies:
RUN set -ex && pip install -r requirements.txt
ADD . /code/
