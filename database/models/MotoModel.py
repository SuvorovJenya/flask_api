from sqlalchemy import Column, Integer
from database.enums.TransportType import TransportType
from database.models.TransportModel import TransportModel
from database.enums.TransportType import TransportType


class MotoModel(TransportModel):

    cylinders = Column(Integer)
    tacts = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": TransportType['MOTO'],
    }
