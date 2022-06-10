from sqlalchemy import Column, Integer, String
from database import Base


class AutoModel(Base):
    __tablename__ = 'auto'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    year_of_production = Column(Integer)
    mileage = Column(Integer)
    body_type = Column(String)
    color = Column(String)
    price = Column(Integer)
