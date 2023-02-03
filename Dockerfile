FROM python:3.11

WORKDIR /socket_app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]