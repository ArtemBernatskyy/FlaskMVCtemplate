from app import db


class User(db.Document):
    email = db.StringField(required=True)
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=200)

