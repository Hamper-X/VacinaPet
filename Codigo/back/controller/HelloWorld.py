from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', default="World")

class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

  def post(self):
    args = parser.parse_args()
    return {'msg': 'Hello there, {}!'.format(args['name'])}