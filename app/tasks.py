import os

from . import celery
from time import sleep
from . import socketio
from app import create_app
from  flask import jsonify
from config import Config
import json
import random


def _handle_global():
    global model


@celery.task(bind=True)
def get_model_json(self):
    pass


@celery.task
def upload_diseases_excel(path):
    pass

@celery.task
def upload_crops_excel(path):
    pass

