from flask import jsonify, request, redirect
from models import Widget 
from flask_sqlalchemy import SQLAlchemy
from crud.widget_crud import get_all_widgets, create_widget, get_widget, update_widget, destroy_widget

@app.route('/')
def home():
    return jsonify(message='Welcome to the main page!')

@app.route('/widgets', methods=['GET', 'POST'])
def widgets():
    if request.method == 'GET':
        return get_all_widgets()
    else: 
        return jsonify(message='route under construction')

@app.route('/widgets', method=['GET', 'POST'])
def create():
    if request.method == 'POST':
        return create_widget()
    else: 
            return jsonify(message='route not available yet')

@app.route('/widgets/<id>', method=['GET', 'POST'])
def show(id):
    if request.method == 'GET':
        return get_widget()
    else:
        return jsonify(message='route not up yet, check back later')

@app.route('/widgets/<id>', method=['PUT'])
def update_widget(id):
    if request.method == 'PUT':
        return update_widget()
    else: 
        return jsonify(message='route coming soon!')

@app.route('/widgets/<id>', method=['DELETE'])
def destroy_widget(id):
    if request.method == 'DELETE':
        return destroy_widget(id)
    else: 
        return jsonify(message='route coming soon')
