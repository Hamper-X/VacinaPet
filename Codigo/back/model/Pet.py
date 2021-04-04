from service.database import db
from model.Clinica import Clinica
from model.Medicamento import Medicamento
from model.Vacina import Vacina

class Pet(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(64))
  especie = db.Column(db.String(64))
  peso = db.Column(db.Float)
  sexo  = db.Column(db.String(1))
  porte  = db.Column(db.String(16))
  nascimento  = db.Column(db.DateTime)
  raca  = db.Column(db.String(32))
  cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
  historico = db.relationship('Clinica', backref='pet', lazy=True)
  medicamento = db.relationship('Medicamento', backref='pet', lazy=True) 
  vacina  = db.relationship('Vacina', backref='pet', lazy=True)

  def __init__(self, nome, especie, peso, sexo, porte, nascimento, raca, cliente_id):
    self.nome = nome
    self.especie = especie
    self.peso = peso
    self.sexo = sexo
    self.porte = porte
    self.nascimento = nascimento
    self.raca = raca
    self.cliente_id = cliente_id