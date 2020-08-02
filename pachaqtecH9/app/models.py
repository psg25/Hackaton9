from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from app import login
from app import db

class User(UserMixin. db.Model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(sb.String(128))
    posts = db.relationship('Post', backref ='autor', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        pass
class Post(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Interger, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
