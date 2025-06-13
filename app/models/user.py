from datetime import datetime
from flask_login import UserMixin
from app import db, bcrypt

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    projects = db.relationship('Project', backref='user', lazy=True)

    def __init__(self, email, username=None, password=None):
        self.email = email
        self.username = username
        if password:
            self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        if not self.password:
            return False
        return bcrypt.check_password_hash(self.password, password)