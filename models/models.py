from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# Users Table
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

# Folders Table
class Folder(db.Model):
    __tablename__ = "folders"

    id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(100), nullable=False)
    is_honeytoken = db.Column(db.Boolean, default=False)

# Logs Table
class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    folder_name = db.Column(db.String(100))
    access_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50))

# Alerts Table
class Alert(db.Model):
    __tablename__ = "alerts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    alert_message = db.Column(db.String(300))
    alert_time = db.Column(db.DateTime, default=datetime.utcnow)