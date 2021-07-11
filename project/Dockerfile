# pull official base image
FROM python:3.9.5-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

ENV AWS_ACCESS_KEY_ID=AKIARQECBKOAVWSC3E6J
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_DEFAULT_REGION=us-east-1
