from app import db
from app import app
from sqlalchemy_utils.types.password import PasswordType

class User(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    email     = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password  = db.Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)
    is_admin  = db.Column(db.Boolean, default=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.email)
