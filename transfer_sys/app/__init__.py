from flask import Flask
# third party
from flask_mongoengine import MongoEngine
# local


app = Flask(__name__)
app.config.from_object('settings')
db = MongoEngine()
db.init_app(app)

import urls
urls.urlpatterns(app)
