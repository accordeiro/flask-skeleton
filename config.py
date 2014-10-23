# -*- coding: utf8 -*-
from app.helpers.env import load_env, env_get
import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))
load_env(paths=[os.path.join(basedir, ".env")])

CSRF_ENABLED = True
SECRET_KEY = env_get('SECRET_KEY')
DEBUG = (env_get('ENVIRONMENT') == 'development')

if env_get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = env_get('DATABASE_URL')

ADMINS = env_get('ADMINS').split(',') if env_get('ADMINS') else []

PV_AWS_ACCESS_KEY = env_get('PV_AWS_ACCESS_KEY')
PV_AWS_SECRET_KEY = env_get('PV_AWS_SECRET_KEY')
PV_POLITICIAN_S3_BUCKET = env_get('PV_POLITICIAN_S3_BUCKET')
