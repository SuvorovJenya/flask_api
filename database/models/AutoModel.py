from sqlalchemy import Column, String
from database.models.TransportModel import TransportModel


class AutoModel(TransportModel):
    complete_set = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "auto",
    }
