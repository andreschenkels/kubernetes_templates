# -*- coding: utf-8 -*-
from flask import Flask
from flask import Response
from flask_sqlalchemy import SQLAlchemy

import json


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


from models.test import Test


def response(body):
    response = Response(json.dumps(body))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'  #'PUT,POST,DELETE'
    return response

@app.route('/', methods=['GET'])
def index():
    result = db.engine.execute("SELECT COUNT(1) FROM tests").first()[0]
    return response('Hello world! {} entries in `tests` table'.format(result))

if __name__ == '__main__':
    app.run(debug=True)
