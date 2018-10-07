# -*- coding: utf-8 -*-
import os


class Config(object):
    # Reading MySQL credentials from environment
    username = os.environ['MYSQL_USERNAME']
    password = os.environ['MYSQL_PASSWORD']
    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@mysql/<DATABASE>'.format(username, password)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'  # for local tests
    SQLALCHEMY_TRACK_MODIFICATIONS = False
