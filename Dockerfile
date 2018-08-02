FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY App ./App

COPY main.py ./

EXPOSE 5000

ENV FLASK_APP=main.py

CMD ["flask", "run"]
