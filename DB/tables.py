from sqlalchemy import Boolean, Column, Integer, String

from db import Model

class Films(Model):
    __tablename__= "films"

    fild_id = Column(Integer, primary_key=True)
    status = Column(String, index=False)
    title = Column(String)
    is_premiere = Column(Boolean)