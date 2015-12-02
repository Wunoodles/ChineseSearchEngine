# -*- coding: utf8 -*-

from flask import Flask, render_template
from flask_restful import Resource, Api
import json
import OutputCollocation

app = Flask(__name__)
api = Api(app)

@app.route('/show')
def show():
    return render_template('show.html')

class index(Resource):
    def get(self):
		return "Welcome to ChineseSerachEngine"

class ChineseSerachEngine(Resource):
    def get(self, key):
        key_e = key.encode('utf8')
        result = OutputCollocation.Collocation(key_e)
        return {'result':result,'input':key_e}

api.add_resource(index, '/')
api.add_resource(ChineseSerachEngine,'/<string:key>')

if __name__ == '__main__':
    app.run(debug=True)
