from app import admin_manager
from app import db
from app.models.user import User
from flask.ext import admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

class RestrictedAccessModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()

admin_manager.add_view(RestrictedAccessModelView(User, db.session, name="Users"))

