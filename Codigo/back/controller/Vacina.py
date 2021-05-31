
from datetime import datetime
from flask_restful import reqparse, Resource
from model.Vacina import Vacina as VacinaModel
from model.Pet import Pet as PetModel
from flask_jwt import jwt_required, current_identity

parser = reqparse.RequestParser()
for arg in ['nome', 'aplicacao', 'estado', 'proxima', 'pet_id']:
  parser.add_argument(arg)

class Vacina(Resource):
  @jwt_required()
  def post(self):
    args = parser.parse_args()
    try:
      newVacina = VacinaModel(args['nome'], datetime.strptime(args["aplicacao"], '%d/%m/%Y'), args['estado'], datetime.strptime(args["proxima"], '%d/%m/%Y'), args['pet_id'])
      newVacina.add()

    except Exception as e:
      print(e)
      return {"error": "Deu problema, olha no log"}, 400

    return {"msg": "{} adicionado ao pet de id {}".format(args['nome'], args['pet_id'])}, 200

  @jwt_required()
  def get(self, pet_id):
    pet = PetModel.query.getById(pet_id)

    if(pet == None or pet.cliente_id != current_identity.id):
      return {"erro": "Esse pet não pertence à você"}, 401

    response = VacinaModel.query.getByPetId(pet_id)

    return [i.serialize for i in response], 200