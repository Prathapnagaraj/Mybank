from mybank import db
from mybank.models import User
# create database
#db.create_all()
# create entry
db.session.add(User("admin","admin@myback","admin", "bangalure"))
db.session.add(User("me", "me@mymail", "password", "none"))
db.session.commit()
