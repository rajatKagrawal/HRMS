from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, func, UniqueConstraint
from werkzeug.security import generate_password_hash, \
    check_password_hash
from settings import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(50))
    k_name = db.Column(db.String(50))

    def __init__(self, username=None, password=None, **kwargs):
        self.username = username
        self.set_password(password)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # def __repr__(self):
    #    return '<User {}>'.format(self.username)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def todict(self):
        return {'username': self.username, 'first_name': self.first_name, 'last_name': self.last_name,
                'user_type': self.user_type.name}

    def todictpass(self):
        return {'username': self.username, 'first_name': self.first_name, 'last_name': self.last_name,
                'user_type': self.user_type.name, 'password': self.password}