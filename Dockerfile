FROM python:3.9-alpine3.13
LABEL maintainer="yadavaalok"

# Install system dependencies
RUN apk add --no-cache build-base

# Copy requirements file
COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-build-deps

# set the path
ENV PATH="/scripts:/py/bin:$PATH"
