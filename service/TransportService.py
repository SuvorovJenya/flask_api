from sqlalchemy.orm import Session
from database.models.AutoModel import AutoModel
from database.models.MotoModel import MotoModel
from database.models.TruckModel import TruckModel


def get_transport_item(
    db: Session,
    model=None,
    year_of_production=None,
    mileage=None,
    body_type=None,
    color=None,
    price=None,
    complete_set=None,
    cylinders=None,
    tacts=None,
    lifting_capacity=None,
    suspension_chassis=None,
    wheel_arrangement=None,
    table_name=None,
):
    all_filters = []
    if model:
        all_filters.append(
            table_name.model == model,
        )
    if year_of_production:
        all_filters.append(
            table_name.year_of_production == year_of_production,
        )
    if mileage:
        all_filters.append(
            table_name.mileage == mileage,
        )
    if body_type:
        all_filters.append(
            table_name.body_type == body_type,
        )
    if color:
        all_filters.append(
            table_name.color == color,
        )
    if price:
        all_filters.append(
            table_name.price == price,
        )
    if complete_set:
        all_filters.append(
            table_name.complete_set == complete_set,
        )
    if cylinders:
        all_filters.append(
            table_name.cylinders == cylinders,
        )
    if tacts:
        all_filters.append(
            table_name.tacts == tacts,
        )
    if lifting_capacity:
        all_filters.append(
            table_name.lifting_capacity == lifting_capacity,
        )
    if suspension_chassis:
        all_filters.append(
            table_name.suspension_chassis == suspension_chassis,
        )
    if wheel_arrangement:
        all_filters.append(
            table_name.wheel_arrangement == wheel_arrangement,
        )
    if table_name == AutoModel:
        return db.query(AutoModel).\
            filter(*all_filters).all()
    if table_name == MotoModel:
        return db.query(MotoModel).\
            filter(*all_filters).all()
    if table_name == TruckModel:
        return db.query(TruckModel).\
            filter(*all_filters).all()
    print(table_name)


def get_transport_by_id(db: Session, id: int, table_name):
    return db.query(table_name).\
        filter(table_name.id == id).first()


def create_transport(db: Session, item, table_name):
    db_item = table_name(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
