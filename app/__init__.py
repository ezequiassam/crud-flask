from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrade = Migrate(app, db)

manager = Manager(app)
# manager.app_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default