#!/usr/bin/env bash

./Social_Network/docker/scripts/wait-for-it.sh postgres:5432 -s -t 30 --

python Social_Network/src/manage.py runserver 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }
