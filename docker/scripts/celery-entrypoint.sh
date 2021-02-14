#!/usr/bin/env bash

cd Social_Network && celery -A src.app.common.celery worker -l info --concurrency=2