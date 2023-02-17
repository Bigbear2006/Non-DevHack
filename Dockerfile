FROM python:3.11.0

ENV PYTHON DONT WRITE BYTECODE 1
ENV PYTHON UNBUFFERED 1

WORKDIR /Devhack

COPY Pipfile Pipfile.lock /Devhack/
RUN pip install pipenv && pipenv install --system

COPY . /Devhack/