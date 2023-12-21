from app.common_functions import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = get_db_url()

engine = create_engine(url=db_url)
LocalSession = sessionmaker(bind=engine)
Base = declarative_base()
