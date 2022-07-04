from sqlalchemy import Column, Integer, String
from database.models.TransportModel import TransportModel
from database.enums.TransportType import TransportType


class TruckModel(TransportModel):

    lifting_capacity = Column(Integer)
    suspension_chassis = Column(String)
    wheel_arrangement = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": TransportType['TRUCK'],
    }
