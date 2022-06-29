from database.models.AutoModel import AutoModel
from database.models.MotoModel import MotoModel
from database.models.TruckModel import TruckModel
from database.enums.TransportType import TransportType


def get_transport_query(db, args, type):
    model = _getModelByType(type)
    return db.query(model).\
        filter_by(**args.dict(exclude_none=True)).all()


def get_tansport_query_by_id(db, id, type):
    model = _getModelByType(type)
    return db.query(model).\
        filter(model.id == id).first()


def add_item_to_model(db, item, type):
    model = _getModelByType(type)
    db_item = model(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)


def _getModelByType(type):
    transport_type_fabric = {
        TransportType['MOTO']: MotoModel,
        TransportType['AUTOS']: AutoModel,
        TransportType['TRUCK']: TruckModel,
    }
    if TransportType.get(type) is None:
        return 'Model not found'
    else:
        return transport_type_fabric[type]
