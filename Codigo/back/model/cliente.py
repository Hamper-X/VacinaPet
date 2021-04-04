from service.database import db

class Cliente(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(256), nullable=False)
  email = db.Column(db.String(512), unique=True, nullable=False)
  senha = db.Column(db.Text, nullable=False)
  pet = db.relationship('Pet', backref='cliente', lazy=True)

  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha

  def __repr__(self):
    return '<Cliente %r>' % self.email
