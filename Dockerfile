# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /ezcite


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .



CMD [ "python3", " ezcitev2beta.py"]