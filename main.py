from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import *
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk import capture_exception, capture_message
import os

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    sentry_sdk.init(
    dsn="https://bbacfd35df9743ff9f67f1910418525b@o1242940.ingest.sentry.io/6397848",
    environment=os.environ.get('FLASK_ENV')
    )
    return app

enviroment = config['development']
app = create_app(enviroment)
jwt = JWTManager(app)
    
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        if username != 'prueba' or password != 'prueba':
            return jsonify({'response': 'Wrong Credentials'}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    except Exception as e:
        capture_exception(e)

@app.route('/state/<name>', methods=['GET'])
@jwt_required()
def get_state(name):
    try:
        result_state = State.query.filter(name=name).first()
        if not result_state:
            error="without results"
            return jsonify(error),204
        results_state = {
            "results_state": {"name": result_state.name, "acronym_renapo":result_state.acronym_renapo,"official_number":result_state.official_number} 
            
        }
        return jsonify(results_state)
    except Exception as e:
        capture_exception(e)


@app.route('/suburb_name/<suburb>', methods=['GET'])
@jwt_required()
def get_suburb_names(suburb):
    try:
        result_suburbs= Postal_Code.query.filter(suburb=suburb).all
        if not result_suburbs:
            error="without results"
            return jsonify(error),204
        results_suburbs = {
            "results_suburb": [{"suburb": result_suburb.suburb, "postal_code":result_suburb.postal_code,"city":result_suburb.city,"municipalty":result_suburb.municipalty} for result_suburb in result_suburbs .items]
            
        }
        return jsonify(results_suburbs)
    except Exception as e:
        capture_exception(e)


if __name__ == "__main__":
    app.run()
