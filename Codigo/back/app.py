from flask import Flask
from flask_restful import Api
from service.database import db
from controller.HelloWorld import HelloWorld
from controller.Cliente import Cliente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://d8xqwtf1pooefomm:zphrgo3avwoclda0@klbcedmmqp7w17ik.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/hhd4sry24dakj5vc?charset=utf8mb4'
api = Api(app)
db.init_app(app)

api.add_resource(HelloWorld, '/api/helloworld')
api.add_resource(Cliente, '/api/cliente')

if __name__ == '__main__':
  app.run(debug=True)