from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://user:password@db:5432/ads_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ожидание БД
for i in range(10):
    try:
        engine.connect()
        break
    except OperationalError:
        print("Waiting for DB...")
        time.sleep(2)