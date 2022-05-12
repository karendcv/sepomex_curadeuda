from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class State(db.Model):
    __tablename__ = 'state'

    id_state = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False) 
    acronym_renapo = db.Column(db.String(255), nullable=False) 
    official_number = db.Column(db.Integer)


class Municipality(db.Model):
    __tablename__ = 'municipality'
    id_municipalty = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False) 
    state_id = db.Column(db.Integer, db.ForeignKey('state.id_state'))
    state = db.relationship(State) 


class Postal_Code(db.Model):
    __tablename__ = 'postal_code'
    id_postal_code = db.Column(db.Integer, primary_key=True)
    suburb = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    municipalty_id = db.Column(db.Integer, db.ForeignKey('municipality.id_municipalty'))
    municipalty = db.relationship(Municipality)
    settlement =  db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(5), nullable=False)

