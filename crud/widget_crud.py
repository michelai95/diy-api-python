from flask import jsonify, redirect
from models import Widget, db

def get_all_widgets():
    all_widgets = Widget.query.all()
    results = []
    for widget in all_widgets:
        results.append(widget.as_dict())
    return jsonify(results)

def create_widget(name, widgets, quantity)
    widget = Widget(id={self.id}, wodgets={self.wodgets}, quantity={self.quantity}, name="{self.name}")
    db.session.add(widget)
    db.session.commit()
    return widget

def get_widget(id):
    widget = Widget.query.get(id)
    if widget: 
        return jsonify(widget.as_dict())
    else: 
        return jsonify({'message': f'cannot find widget id {id}'})

def update_widget(id, name, widgets, quantity):
    widget = Widget.query.get(id)
    if widget:
        widget.name = name or widget.name
        widget.widgets = widgets or widget.widgets
        widget.quantity = quantity or widget.quantity
        db.session.commit()
        return jsonify(widget.as_dict())
    else: 
        return jsonify({'message': f'cannot find widget id {id}'})

def destroy_widget(id):
    widget = Widget.query.get(id)
    if widget:
        db.session.delete(widget)
        db.session.commit()
        return redirect('/widgets')
    else: 
        return jsonify({'message': f'cannot find widget id {id}'})