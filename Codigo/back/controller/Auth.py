from model.cliente import Cliente as ClienteModel

def authenticate(username, password):
  user = ClienteModel.query.getByEmail(username)
  if user and user.senha == password:
    return user

def identity(payload):
  user_id = payload['identity']
  return ClienteModel.query.getById(user_id)