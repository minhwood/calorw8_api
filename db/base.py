from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs.settings import settings

engine = create_engine(settings.POSTGRES_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)