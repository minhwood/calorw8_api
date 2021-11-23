## Fast API Code Base Template

- Python version: 3.8.10
- Framework: Fast API

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

POSTGRES_SERVER: Postgres Host
POSTGRES_USER: Postgres user name
POSTGRES_PASSWORD: Postgres password
POSTGRES_DB: Postgres database name
POSTGRES_DATABASE_URI: Postgres database URI for connection
DATASOURCE: Data source of the Cannada Food report for database migration purpose