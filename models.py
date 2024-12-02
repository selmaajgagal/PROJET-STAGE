from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    _tablename_ = 'feedback'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    date_of_stay = Column(Date, nullable=False)
    comment = Column(Text, nullable=True)
    rating_proprete = Column(Integer, nullable=True)
    rating_personnel = Column(Integer, nullable=True)
