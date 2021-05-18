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
    try:
      novo_cliente = ClienteModel(args['nome'], args['email'], args['senha'])
      db.session.add(novo_cliente)
      db.session.commit()
    except Exception as e:
      print(e)
      return {'erro': 'Algo deu errado. Favor referir ao log do sistema'}

    return {'msg': 'Novo usuário adicionado'}