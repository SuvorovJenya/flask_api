from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models import db, AutosModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()
    

class AutosView(Resource):

    def get(self):
        autos = AutosModel.query.all()
        return {'Autos':list(x.json() for x in autos)}

    
    def post(self):
        data = request.get_json()
        new_auto = AutosModel(data['model'], data['year_of_production'], data['mileage'],
                              data['body_type'], data['color'], data['horsepower'], data['price'])
        db.session.add(new_auto)
        db.session.commit()
        return new_auto.json(),201
    
class Autos_get_one(Resource):
    
    def get(self, pk):
        auto = AutosModel.query.filter_by(id=pk).first()
        if auto:
            return auto.json()
        return {'message':'book not found'},404
    
    
class Autos_color(Resource):
    
    def get(self, color):
        auto = AutosModel.query.filter_by(color=color).all()
        if auto:
            return {'Autos':list(x.json() for x in auto)}
        return {'message':'book not found'},404


api.add_resource(AutosView, '/autos')
api.add_resource(Autos_get_one, '/autos/<int:pk>')
api.add_resource(Autos_color, '/autos/<string:color>')

if __name__ == "__main__":
    app.run()
