from typing import Generator

from db.base import SessionLocal

def repository() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()