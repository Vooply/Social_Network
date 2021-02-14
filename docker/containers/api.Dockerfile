FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /Social_Network

RUN chmod +x /Social_Network/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /Social_Network/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /Social_Network/requirements.txt
