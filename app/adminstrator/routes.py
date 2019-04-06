import json
import os
from datetime import datetime
from secrets import token_urlsafe
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
import cloudinary
import cloudinary.api
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import pycountry



cloudinary.config(
    cloud_name='intelecs',
    api_key='815186897625597',
    api_secret='u0IjmaHsoWvyHbuFpoYtCYmL61U'
)
