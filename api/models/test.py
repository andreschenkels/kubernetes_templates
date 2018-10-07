# -*- coding: utf-8 -*-
from app import db


class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(16))
    val = db.Column(db.String(256))

    def __init__(self, key, val, result_no_stop_words):
        self.key = key
        self.val = val

    def __repr__(self):
        return '<id {}>'.format(self.id)
