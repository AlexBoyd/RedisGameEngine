FROM python:alpine

RUN pip install redis

CMD [ "python", "./src/Main.py" ]