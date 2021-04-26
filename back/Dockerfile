FROM python:3.8-alpine

RUN mkdir -p /src

WORKDIR /src

COPY requirements.txt /src

RUN pip3 install -r requirements.txt

COPY . /src

EXPOSE 5000

CMD python3 app.py