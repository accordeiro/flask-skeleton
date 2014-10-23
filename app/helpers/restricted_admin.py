from flask import redirect, url_for
from flask.ext import admin
from flask.ext.login import current_user

class RestrictedAdminIndexView(admin.AdminIndexView):
    @admin.expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('login')+'?next=/admin/')
        return super(RestrictedAdminIndexView, self).index()

    @admin.expose('/login/')
    def login_view(self):
        return redirect(url_for('login'))
