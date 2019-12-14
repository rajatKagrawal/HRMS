from flask import Flask
from models import User
from settings import app, db

db.create_all()
db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
