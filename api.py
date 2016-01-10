# -*- coding: utf8 -*-

from flask import Flask, render_template
from flask_restful import Resource, Api
import json
import OutputCollocation
import os

app = Flask(__name__)
api = Api(app)

port = int(os.environ.get('PORT', 5000))

@app.route('/show')
def show():
    return render_template('show.html')

class index(Resource):
    def get(self):
		return "Welcome to ChineseSerachEngine"

class ChineseSerachEngine(Resource):
    def get(self, key):
        if(key >= u'\u4e00' and key <= u'\u9fa5'):
            key_e = key.encode('utf8')
            POS = OutputCollocation.Give_Word_Speech(key_e)
            if(POS == 'N'):
                result = 'N'
                collocation = 'N'
            else:
                POS_in = POS.strip()
                result = OutputCollocation.Recommendation(POS_in)
                collocation = OutputCollocation.Collocation(key_e)
        else:
            result = 'NULL'
            collocation = 'NULL'
        return {'result':result,'input':key,'collocation':collocation}

@app.route('/table')
def table():
    return render_template('table.html')


api.add_resource(index, '/')
api.add_resource(ChineseSerachEngine,'/<string:key>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)
