from service.database import db

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
  historico = db.Relationship('Clinica', backred='pet', lazy=True)
  medicamento = db.Relationship('Medicamento', backred='pet', lazy=True) 
  vacina  = db.Relationship('Vacina', backred='pet', lazy=True)

  def __init__(self, nome, especie, peso, sexo, porte, nascimento, raca, cliente_id):
    self.nome = nome
    self.especie = especie
    self.peso = peso
    self.sexo = sexo
    self.porte = porte
    self.nascimento = nascimento
    self.raca = raca
    self.cliente_id = cliente_id