FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /Social_Network

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /Social_Network/requirements.txt

WORKDIR Social_Network/src