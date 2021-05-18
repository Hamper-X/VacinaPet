from service.database import db

class Vacina(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(128))
  aplicacao = db.Column(db.DateTime)
  estado = db.Column(db.String(256))
  proxima = db.Column(db.DateTime)
  pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)

  def __init__(self, nome, aplicacao, estado, proxima, pet_id):
    self.nome = nome
    self.aplicacao = aplicacao
    self.estado = estado
    self.proxima = proxima
    self.pet_id = pet_id