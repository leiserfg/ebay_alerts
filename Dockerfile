FROM python:alpine3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

ONBUILD RUN pip install pipenv
ONBUILD RUN apk add --update --no-cache gcc libxslt-dev
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system
ADD . /code/
