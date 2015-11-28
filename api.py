# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

@app.route('/show')
def show():
    return render_template('show.html')

class index(Resource):
    def get(self):
		return "Welcome to ChineseSerachEngine"
        #return {'帥哥': '偉宏', '正妹': '旻諺'}

api.add_resource(index, '/')

if __name__ == '__main__':
    app.run(debug=True)