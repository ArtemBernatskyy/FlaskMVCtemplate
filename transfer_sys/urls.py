from app.jobs.urls import blueprint as task_urls
from app.users.urls import blueprint as users_urls
from app.auth.urls import blueprint as auth_urls


def urlpatterns(app):
    app.register_blueprint(users_urls, url_prefix='/users')
    app.register_blueprint(task_urls, url_prefix='/jobs')
    app.register_blueprint(auth_urls, url_prefix='/auth')
