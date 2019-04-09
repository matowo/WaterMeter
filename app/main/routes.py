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
from app.models import User, BillingAddress, Balance
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

@bp.route('/meters')
@login_required
def meters():
    user = User.query.filter_by(secure_token=current_user.secure_token).first()
    meters = user.meters
    balances = user.balance
    return render_template('main/meters.html', title=_('Meters'), meters=meters, balances=balances)

@bp.route('/pay', methods=['GET', 'POST'])
@login_required
def pay():
    pass

@bp.route('/add-billing', methods=['GET', 'POST'])
@login_required
def add_billing():
    form = BillingAddressForm()
    if form.validate_on_submit():
        billing = BillingAddress(
            address_1=form.address_line.data,
            address_2=form.address_line_1.data,
            secure_token=token_urlsafe(16)
        )
        db.session.add(billing)
        db.session.commit()
        flash('Billing Address is Set up')
        return redirect(url_for('main.user', token=current_user.secure_token))
    return render_template('main/add_billing.html', title=_('Add Billing Address'), form=form)

@bp.route('/edit-billing/<string:token>', methods=['GET', 'POST'])
@login_required
def edit_billing(token):
    address = BillingAddress.query.filter_by(secure_token=token).first()
    if address is None: abort(404)

    form = EditBillingAddressForm()
    if form.validate_on_submit():
        address.address_1 = form.address_line.data
        address.address_2 = form.address_line_1.data
        db.session.commit()
        flash('Billing Address has been updated')
        return redirect(url_for('main.user', token=current_user.secure_token))
    form.address_line.data = address.address_1
    form.address_line_1.data = address.address_2

    return render_template('main/eedit_billing.html', title=_('Edit Billing Address'), form=form)


