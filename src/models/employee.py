
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
  """
  Employee Model
  """

  # table name
  __tablename__ = 'employee'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  hashed_password = db.Column(db.String(128), nullable=True)
  salary = db.Column(db.String(30), nullable=True)
  designation = db.Column(db.String(30), nullable=True)

  def __init__(self, id, name, email, salary, designation):
        self.id = id
        self.name = name
        self.email = email
        self.salary = salary
        self.designation = designation
