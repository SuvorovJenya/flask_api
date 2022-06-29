from sqlalchemy.orm import Session
from database.models.AutoModel import AutoModel
from database.models.MotoModel import MotoModel
from database.models.TruckModel import TruckModel
from database.enums.TransportType import TransportType


def get_transport_item(
    db: Session,
    args,
    model_type,
):
    model = _getModelByType(model_type)
    return db.query(model).filter_by(**args.dict(exclude_none=True)).all()


def get_transport_by_id(db: Session, id: int, model_type):
    model = _getModelByType(model_type)
    return db.query(model).\
        filter(model.id == id).first()


def create_transport(db: Session, item, model_type):
    model = _getModelByType(model_type)
    db_item = model(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def _getModelByType(model_type):
    transporttypefabric = {
        TransportType['MOTO']: MotoModel,
        TransportType['AUTOS']: AutoModel,
        TransportType['TRUCK']: TruckModel,
    }
    if TransportType.get(model_type) is None:
        return 'Error'
    else:
        return transporttypefabric[model_type]
