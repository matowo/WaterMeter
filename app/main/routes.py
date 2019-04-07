import json
import os
from datetime import datetime

import requests
from secrets import token_urlsafe
from flask import render_template, flash, redirect, url_for, request, \
    g, current_app, json, send_from_directory, jsonify, abort
from flask_babel import _, get_locale
from flask_ckeditor import upload_fail, upload_success
from flask_login import current_user, login_required
from app import db
from app.main import bp
from app.main.forms import BillingAddressForm, EditBillingAddressForm
from app.models import User
from .. import mqtt
from .. import socketio
from app.main.forms import EditProfileForm




@bp.route('/')
@bp.route('/home')
#@login_required
def home():
    return render_template('landing/index.html')



@bp.route('/index')
@bp.route('/dashboard')
@login_required
def index():
    return render_template('main/index.html')

@bp.route('/user/<string:token>')
@login_required
def user(token):
    user = User.query.filter_by(secure_token=token).first()
    if user is None: abort(404)
    return render_template('main/user.html', title=_(user.username), user=user)

@bp.route('/pay')
@login_required
def pay():
    pass

@bp.route('/add-billing')
@login_required
def add_billing():
    form = EditBillingAddressForm()
    return render_template('main/add_billing.html', title=_('Add Billing Address'), form=form)

@bp.route('/edit-billing')
@login_required
def edit_billing():
    pass


