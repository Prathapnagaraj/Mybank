from mybank import db
from mybank import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    place =db.Column(db.String, nullable=False)

    def __init__(self, name, email, password, place):
        self.name = name
        self.email = email
        self.place = place
        self.password =bcrypt.generate_password_hash(password)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name {}'.format(self.name)