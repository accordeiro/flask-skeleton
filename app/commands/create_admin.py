from app import db
from app.helpers.manager import manager
from app.models.user import User

import traceback

@manager.command
def create_admin(email, password):
    try:
        u = User(email=email, password=password, is_admin=True)
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        traceback.print_exc()
    else:
        print "Successfully created admin user with e-mail %s" % email
