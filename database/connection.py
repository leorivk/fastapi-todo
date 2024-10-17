from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:todo@127.0.0.1:3306/todo"

engine = create_engine(DATABASE_URL, echo=True)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Generator
def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()

