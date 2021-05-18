from service.database import db
from model.Pet import Pet
from flask_sqlalchemy import BaseQuery

class ClienteMethods(BaseQuery):
  def getByEmail(self, email, default=None):
    return self.filter_by(email=email).first()
  def getById(self, id):
    return self.filter_by(id=id).first()

class Cliente(db.Model):
  query_class = ClienteMethods
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(256), nullable=False)
  email = db.Column(db.String(512), unique=True, nullable=False)
  senha = db.Column(db.Text, nullable=False)
  pet = db.relationship('Pet', backref='cliente')

  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha

  def __repr__(self):
    return '<Cliente %r>' % self.email

