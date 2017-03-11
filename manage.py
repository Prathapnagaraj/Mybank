#from flask_script import Manager
from flask.ext.script import Manager
#from flask.ext.migrate import Migrate,MigrateCommand
from flask_migrate import Migrate,MigrateCommand
import os

from mybank import app,db
app.config.from_object('config.DevelopmentConfig')
migrate=Migrate(app, db)
manager=Manager(app)
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()
