# -*- coding: utf8 -*-

from flask import Flask, render_template
from flask_restful import Resource, Api
import json
import main
import os
import jieba
jieba.cut('我', cut_all=False)
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
        result = 'NULL'
        if(key >= u'\u4e00' and key <= u'\u9fa5'):
            key_e = key.encode('utf8')
            result = main.Chinese_sentence_system(key_e)
        return {'result':result,'input':key}

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/table_complete')
def table_complete():
    return render_template('table_complete.html')

api.add_resource(index, '/')
api.add_resource(ChineseSerachEngine,'/<string:key>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)
