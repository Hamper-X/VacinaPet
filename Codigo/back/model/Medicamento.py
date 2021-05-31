from service.database import db
from flask_sqlalchemy import BaseQuery

class MedicamentoMethods(BaseQuery):
  def getByPetId(self, pet_id):
    return self.filter_by(pet_id = pet_id).all()


class Medicamento(db.Model):
  query_class = MedicamentoMethods
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(64))
  dosagem = db.Column(db.String(64))
  horario = db.Column(db.String(128))
  estado = db.Column(db.String(256))
  observacao = db.Column(db.String(512))
  pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)

  def __init__(self, nome, dosagem, horario, estado, observacao, pet_id):
    self.nome = nome
    self.dosagem = dosagem
    self.horario = horario
    self.estado = estado
    self.observacao = observacao
    self.pet_id = pet_id

  @property
  def serialize(self):
    return {
      'id': self.id,
      'nome': self.nome,
      'dosagem': self.dosagem,
      'horario': self.horario,
      'estado': self.estado,
      'observacao': self.observacao
    }

  def add(self):
    db.session.add(self)
    db.session.commit()