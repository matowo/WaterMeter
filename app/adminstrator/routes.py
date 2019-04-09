import json
import os
from datetime import datetime
from secrets import token_urlsafe, randbits
import requests
from flask import render_template, flash, redirect, url_for, request, \
    g, current_app, json, send_from_directory, jsonify,abort
from flask_babel import _, get_locale
from flask_ckeditor import upload_fail, upload_success
from flask_login import current_user, login_required
from app import db
from app.adminstrator import bp
from .. import mqtt
from .. import socketio
from app.models import Meter, User


@bp.route('/meters')
@login_required
def meters():
    meters = Meter.query.all()
    return render_template('admin/meters.html', meters=meters, title=_('Meters'))

@bp.route('meter/<token>')
def meter(token):
    meter = Meter.query.filter_by(secure_token=token).first()
    users = User.query.all()
    return render_template('admin/meter.html', meter=meter, title=_(token), users=users)

@bp.route('/assign-meter/<string:token>/<string:username>')
@login_required
def assign_meter(token, username):
    meter = Meter.query.filter_by(secure_token=token).first()

    users = User.query.all()
    for user in users:
        if user.id == meter.user_id:
            flash('This Meter Alredad assigned to {}'.format(user.username))
            return redirect(url_for('administrator.meter', token=token))
    user = User.query.filter_by(username=username).first()

    if user.meters.count() > 0:
        flash('User already have Meter assigned to')
        return redirect(url_for('administrator.meter', token=token))

    meter.user_id = user.id
    db.session.commit()
    flash('Everything went well, now {} owns meter {}'.format(username, token))
    return redirect(url_for('administrator.meter', token=token))




@bp.route('/revoke-meter/<string:token>/<string:username>')
@login_required
def revoke_meter(token, username):

    user = User.query.filter_by(username=username).first()
    meter = Meter.query.filter_by(user_id=user.id).first()

    meter.user_id = None
    db.session.commit()
    flash('{} no longer owns meter {}'.format(username, token))
    return redirect(url_for('administrator.meter', token=token))

@bp.route('generete-meter')
@login_required
def generate():
    meter = Meter(
        secure_token=randbits(36)
    )
    db.session.add(meter)
    db.session.commit()
    flash('Meter Number Generated')
    return redirect(url_for('administrator.meters'))

@bp.route('/remove-meter/<string:token>')
@login_required
def remove_meter():
    pass