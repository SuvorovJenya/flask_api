from sqlalchemy import Column, Integer
from database.models.TransportModel import TransportModel


class MotoModel(TransportModel):

    cylinders = Column(Integer)
    tacts = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": "moto",
    }
