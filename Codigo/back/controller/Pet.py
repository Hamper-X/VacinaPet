from logging import exception
from flask_restful import reqparse, Resource
from flask_jwt import jwt_required, current_identity
from model.Pet import Pet as PetModel
from datetime import datetime

parser = reqparse.RequestParser()
for arg in ['nome', 'especie', 'peso', 'sexo', 'porte', 'nascimento', 'raca']:
  parser.add_argument(arg)

class Pet(Resource):
  @jwt_required()
  def post(self):
    args = parser.parse_args()
    try:

      newPet = PetModel(args['nome'], args['especie'], args['peso'], args['sexo'], args['porte'], args['nascimento'], args['raca'], current_identity.id)
      newPet.add()

    except Exception as e:
      print(e)
      return {"error": "Deu problema, olha no log"}

    return {"msg": "{} adicionado na conta de {}".format(args['nome'], current_identity.email)}

  @jwt_required()
  def get(self):
    
    response = PetModel.query.getByClienteId(current_identity.id)
    return [i.serialize for i in response]