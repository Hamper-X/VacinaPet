from flask_restful import reqparse, Resource
from model.cliente import Cliente as ClienteModel
from service.database import db

parser = reqparse.RequestParser()
for arg in ['nome', 'email', 'senha']:
  parser.add_argument(arg)

class Cliente(Resource):
  # cadastro
  def post(self):
    args = parser.parse_args()
    novo_cliente = ClienteModel(args['nome'], args['email'], args['senha'])
    db.session.add(novo_cliente)
    db.session.commit()
    return {'msg': 'Novo usuário adicionado'}