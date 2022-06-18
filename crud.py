from sqlalchemy.orm import Session
import models
import schemas


def get(
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
            models.AutoModel.model == model,
            )
    if year_of_production:
        all_filters.append(
            models.AutoModel.year_of_production == year_of_production,
            )
    if mileage:
        all_filters.append(
            models.AutoModel.mileage == mileage,
            )
    if body_type:
        all_filters.append(
            models.AutoModel.body_type == body_type,
            )
    if color:
        all_filters.append(
            models.AutoModel.color == color,
            )
    if price:
        all_filters.append(
            models.AutoModel.price == price,
            )
    return db.query(models.AutoModel).\
        filter(*all_filters).all()


def get_by_id(db: Session, auto_id: int):
    return db.query(models.AutoModel).\
        filter(models.AutoModel.id == auto_id).first()


def create(db: Session, item: schemas.AutoModel):
    db_item = models.AutoModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
