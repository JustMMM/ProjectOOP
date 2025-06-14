from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SQLiteSessionFactory:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, connect_args={"check_same_thread": False})
        self.Session = sessionmaker(bind=self.engine)

    def create_session(self):
        return self.Session()