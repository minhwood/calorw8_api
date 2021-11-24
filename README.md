## Fast API Code Base Template

- Python version: 3.8.10
- Framework: Fast API
- Data was extracted from Goverment of Cannada Nutrient File (2015) [https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/canadian-nutrient-file-2015-download-files.html]

### Generate Alembic auto migration script
```
alembic revision --autogenerate -m "Information about database commit"
```

### Migrate database
```
alembic upgrade head
```

### Downgrade database to default
```
alembic downgrade base
```

### Start server
```
uvicorn main:app --reload
```

### Environment varriable:

- **POSTGRES_SERVER**: Postgres Host
- **POSTGRES_USER**: Postgres user name
- **POSTGRES_PASSWORD**: Postgres password
- **POSTGRES_DB**: Postgres database name
- **POSTGRES_DATABASE_URI**: Postgres database URI for connection
- **DATASOURCE**: Data source of the Cannada Food report for database migration purpose