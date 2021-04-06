FROM python:3-alpine3.12

COPY code /opt/mqtt_utils

ENV PATH /opt/mqtt_utils:$PATH

WORKDIR /opt/mqtt_utils

RUN pip install --no-cache-dir -U -r requirements.txt
