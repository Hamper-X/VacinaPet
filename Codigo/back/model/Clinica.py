from service.database import db

class Clinica(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(256))
  veterinario = db.Column(db.String(256))
  sintomas = db.Column(db.String(512))
  prescricao = db.Column(db.String(1024))
  pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)

  def __init__(self, nome, veterinario, sintomas, prescricao, pet_id):
    self.nome = nome
    self.veterinario = veterinario
    self.sintomas = sintomas
    self.prescricao = prescricao
    self.pet_id = pet_id

  def __repr__(self):
      return '<Clinica>'

  @property
  def serialize(self):
    return {
      'id': self.id,
      'nome': self.nome,
      'veterinario': self.veterinario,
      'sintomas': self.sintomas,
      'prescricao': self.prescricao,
      'pet_id': self.pet_id
    }

  def add(self):
    db.session.add(self)
    db.session.commit()