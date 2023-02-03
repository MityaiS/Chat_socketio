FROM python:3.11

WORKDIR /socket_app

COPY ["template"]
RUN pip install -r requirements.txt
