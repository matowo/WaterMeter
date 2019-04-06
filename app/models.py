import base64
from datetime import datetime, timedelta
from hashlib import md5
from markdown import markdown
import bleach
import json
import os
from time import time
from flask import current_app, url_for
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import redis
import rq
from app import db, login, marshmallow

"""
#--- User Management Model --- #

"""




class User(UserMixin, db.Model):
    # TODO: User Account verification
    """
    User model
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    secure_token = db.Column(db.String(128), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # Phone number authentication and verification
    phone_number = db.Column(db.String)
    country_code = db.Column(db.String)
    phone_number_confirmed = db.Column(db.Boolean, default=False)

    notifications = db.relationship('Notification', backref='user', lazy='dynamic')





    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Sensor(): pass

class Reading(): pass


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    secure_token = db.Column(db.String(128), index=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Gallery(db.Model):
    __tablename__ = 'galleries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    secure_token = db.Column(db.String(128), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    image_url = db.Column(db.String(128))


class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    secure_token = db.Column(db.String(128), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)

    def is_read(self): return self.read

    def set_read(self): self.read = True


class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'
login.anonymous_user = AnonymousUser

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


"""
#--- Crop Management Database Model --- #
"""

