# -*- coding: utf-8 -*-
"""
  author:wnl
  date: 2018-12-7
"""
import os

from sayhello import app

dev_db = 'mysql+pymysql://root:root.123@192.168.100.105:3306/sayhello2'

SECRET_KEY = os.getenv('SECRRET','secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',dev_db)

