from sqlalchemy.orm import Session
import models
import schemas


def get_autos(db: Session, color=None):
    if color:
        return db.query(models.AutoModel).\
            filter(models.AutoModel.color == color).all()
    else:
        return db.query(models.AutoModel).all()


def get_autos_one(db: Session, auto_id: int):
    return db.query(models.AutoModel).\
        filter(models.AutoModel.id == auto_id).first()


def create_auto(db: Session, item: schemas.AutoModel):
    db_item = models.AutoModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
