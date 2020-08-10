from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/diyapi'

db = SQLAlchemy(app)

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = db.Column(db.Integer, primary_key=True)
    wodgets = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'Widget(id={self.id}, wodgets={self.wodgets}, quantity={self.quantity}, name="{self.name}")'