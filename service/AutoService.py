from sqlalchemy.orm import Session
from database.models.AutoModel import AutoModel
from schemas.AutoSchemas import AutoSchemas


def get_auto_item(
    db: Session,
    model=None,
    year_of_production=None,
    mileage=None,
    body_type=None,
    color=None,
    price=None,
):
    all_filters = []
    if model:
        all_filters.append(
            AutoModel.model == model,
        )
    if year_of_production:
        all_filters.append(
            AutoModel.year_of_production == year_of_production,
        )
    if mileage:
        all_filters.append(
            AutoModel.mileage == mileage,
        )
    if body_type:
        all_filters.append(
            AutoModel.body_type == body_type,
        )
    if color:
        all_filters.append(
            AutoModel.color == color,
        )
    if price:
        all_filters.append(
            AutoModel.price == price,
        )
    return db.query(AutoModel).\
        filter(*all_filters).all()


def get_by_id(db: Session, auto_id: int):
    return db.query(AutoModel).\
        filter(AutoModel.id == auto_id).first()


def create(db: Session, item: AutoSchemas):
    db_item = AutoModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
