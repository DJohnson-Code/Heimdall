import os

from sqlalchemy import create_engine, text 
from sqlalchemy.orm import sessionmaker


def get_database_url() -> str: 
    url = os.environ.get("DATABASE_URL")

    if not url: 
        raise RuntimeError(
            "The database url is not set. Add it to .env "
            "load_dotenv() needs to run before importing heimdall.db."
        )
    return url

engine = create_engine(get_database_url())
SessionLocal = sessionmaker(bind=engine)

def check_db() -> None: 
    with engine.connect() as conn: 
        conn.execute(text("SELECT 1"))
