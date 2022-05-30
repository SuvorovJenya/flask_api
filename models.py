from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AutosModel(db.Model):
    __tablename__ = 'autos'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80))
    year_of_production = db.Column(db.Integer())
    mileage = db.Column(db.Integer())
    body_type = db.Column(db.String(80))
    color = db.Column(db.String(80))
    horsepower = db.Column(db.Integer())
    price = db.Column(db.Integer())


    def __init__(self, model, year_of_production, mileage,
                 body_type, color, horsepower, price):
        self.model = model
        self.year_of_production = year_of_production
        self.mileage = mileage
        self.body_type = body_type
        self.color = color
        self.horsepower = horsepower
        self.price = price

    def json(self):
        return {"year_of_production":self.year_of_production,
                "mileage":self.mileage, "body_type":self.body_type, "color":self.color,
                "horsepower":self.horsepower, "price":self.price}
