from flask import Flask
from flask_restful import Api
from controller.HelloWorld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/api/helloworld')

if __name__ == '__main__':
  app.run(debug=True)