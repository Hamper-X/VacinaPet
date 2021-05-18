from datetime import timedelta
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from service.database import db
from controller.Cliente import Cliente
from controller.Auth import authenticate, identity
from controller.Pet import Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://d8xqwtf1pooefomm:zphrgo3avwoclda0@klbcedmmqp7w17ik.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/hhd4sry24dakj5vc?charset=utf8mb4'
app.config['SECRET_KEY'] = 'ninguemsabeessesegredosuperobscuro'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
jwt = JWT(app, authenticate, identity)
api = Api(app)
db.init_app(app)

api.add_resource(Cliente, '/api/cliente')
api.add_resource(Pet, '/api/pet')

if __name__ == '__main__':
  app.run(debug=True)