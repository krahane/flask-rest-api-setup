import os

from src.app import create_app
from src.models.employee import db


if __name__ == '__main__':
  # env_name = os.getenv('FLASK_ENV')
  app = create_app('development')
  # run app 
  with app.app_context():
    db.create_all()
  app.run()