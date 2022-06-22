from sqlalchemy import Column, Integer, String
from database.db import Base


class TransportModel(Base):
    __tablename__ = 'transport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    year_of_production = Column(Integer)
    mileage = Column(Integer)
    body_type = Column(String)
    color = Column(String)
    price = Column(Integer)
    orm_type = Column(String(50))

    __mapper_args__ = {
        "polymorphic_on": orm_type,
        "polymorphic_identity": "transport",
    }
