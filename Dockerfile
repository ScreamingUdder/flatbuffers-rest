FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt ./
COPY ./streaming-data-types/schemas /streaming-data-types/schema

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
