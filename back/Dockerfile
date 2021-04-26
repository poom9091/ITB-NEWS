FROM python:3.8-alpine

RUN mkdir -p /src

WORKDIR /src

COPY requirements.txt /src

RUN pip install -r requirements.txt

COPY . /src

EXPOSE 5000

CMD python server.py