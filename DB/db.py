from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from data.configuration import CONNECTION_DB

Model = declarative_base(name="Model")

engine = create_engine(
    CONNECTION_DB
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocomit=False
)

session = Session()