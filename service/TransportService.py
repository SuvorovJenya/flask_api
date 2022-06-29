from sqlalchemy.orm import Session
from database.models.AutoModel import AutoModel
from database.models.MotoModel import MotoModel
from database.models.TruckModel import TruckModel
from database.enums.TransportType import TransportType


def get_transport(
    db: Session,
    args,
    type,
):
    model = _getModelByType(type)
    return db.query(model).\
        filter_by(**args.dict(exclude_none=True)).all()


def get_transport_by_id(db: Session, id: int, type):
    model = _getModelByType(type)
    return db.query(model).\
        filter(model.id == id).first()


def create_transport(db: Session, item, type):
    model = _getModelByType(type)
    db_item = model(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def _getModelByType(type):
    _transporttypefabric = {
        TransportType['MOTO']: MotoModel,
        TransportType['AUTOS']: AutoModel,
        TransportType['TRUCK']: TruckModel,
    }
    if TransportType.get(type) is None:
        return 'Model not found'
    else:
        return _transporttypefabric[type]
