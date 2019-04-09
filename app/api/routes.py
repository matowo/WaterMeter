import json
import os
from datetime import datetime
from secrets import token_urlsafe
import requests
from flask import render_template, flash, redirect, url_for, request, \
    g, current_app, json, send_from_directory, jsonify,abort
from flask_babel import _, get_locale
from flask_login import current_user, login_required
from app import db, marshmallow
from app.models import User
from app.api import bp



@bp.route('/user-data/<string:token>', methods=['GET'])
def user_data(token):
    user = User.query.filter_by(secure_token=token).first()

    return jsonify(user.to_dict())

@bp.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result.data)


@bp.route('/update-data/<string:token>/<string:user_token>', methods=['POST'])
def update_data(token, user_token):
    pass
