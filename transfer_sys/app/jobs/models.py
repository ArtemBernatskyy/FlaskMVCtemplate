from app import db

from app.users.models import User


class Job(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)
    content = db.FileField()
