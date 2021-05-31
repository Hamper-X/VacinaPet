from service.database import db
from flask_sqlalchemy import BaseQuery
from datetime import datetime

class VacinaMethods(BaseQuery):
  def getByPetId(self, pet_id):
    return self.filter_by(pet_id = pet_id).all()

class Vacina(db.Model):
  query_class = VacinaMethods
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

  @property
  def serialize(self):
    return {
      'id': self.id,
      'nome': self.nome,
      'aplicacao': self.aplicacao.strftime("%d/%m/%Y"),
      'estado': self.estado,
      'proxima': self.proxima.strftime("%d/%m/%Y"),
    }

  def add(self):
    db.session.add(self)
    db.session.commit()