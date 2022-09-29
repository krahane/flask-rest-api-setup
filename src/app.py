import imp
from flask import Flask

from .config import app_config
from flasgger import Swagger
from src.swagger import template, swagger_config
from src.views.route import emp_api
from src.models.employee import db


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)
  SWAGGER={
    'title':"Employees API",
    'uiversion':3
  }
  app.config.from_object(app_config['development'])
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/demo'
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.secret_key = 'secret string'
  app.register_blueprint(emp_api)
  Swagger(app, config=swagger_config, template=template)
  db.init_app(app)

  return app
