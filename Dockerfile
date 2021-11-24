FROM python:3.8.12-slim-buster

WORKDIR /app
COPY . .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install -r requirements.txt
ENV POSTGRES_SERVER=localhost:5432
ENV POSTGRES_USER=developer
ENV POSTGRES_PASSWORD=developer
ENV POSTGRES_DB=calorw8_api
ENV POSTGRES_DATABASE_URI=postgresql+psycopg2://developer:developer@localhost:5432/calorw8_api
ENV DATASOURCE=/home/oliverwood98/Documents/CanadaFoodNutrientDatabase/cnf-fcen-csv

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]