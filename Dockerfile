FROM python:3.8.12-slim-buster

WORKDIR /app
COPY . .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install -r requirements.txt
ENV POSTGRES_SERVER=${POSTGRES_SERVER}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_DATABASE_URI=${POSTGRES_DATABASE_URI}
ENV DATASOURCE=${DATASOURCE}

RUN chmod +x start.sh

CMD ["./start.sh"]