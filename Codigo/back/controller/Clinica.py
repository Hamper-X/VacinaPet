from flask_restful import reqparse, Resource
from model.Clinica import Clinica as ClinicaModel
from model.Pet import Pet as PetModel
from flask_jwt import jwt_required, current_identity

parser = reqparse.RequestParser()
for arg in ['nome', 'veterinario', 'sintomas', 'prescricao', 'pet_id']:
  parser.add_argument(arg)

class Clinica(Resource):
  @jwt_required()
  def post(self):
    args = parser.parse_args()
    pet = PetModel.query.getById(args['pet_id'])

    if(pet == None or pet.cliente_id != current_identity.id):
      return {"erro": "Esse pet não pertence à você"}, 401

    newClinica = ClinicaModel(args['nome'], args['veterinario'], args['sintomas'], args['prescricao'], args['pet_id'])
    newClinica.add()
    return {"msg": "novo histórico de consulta adicionado"}, 200

  def get(self):
    return