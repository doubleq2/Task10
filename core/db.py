from sqlalchemy import create_engine  
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db_string = "postgresql+psycopg2://qq224:123@localhost/ts10"

engine = create_engine(db_string)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()