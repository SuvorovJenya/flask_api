from sqlalchemy import Column, String
from database.models.TransportModel import TransportModel
from database.enums.TransportType import TransportType


class AutoModel(TransportModel):
    complete_set = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": TransportType['AUTOS'],
    }
