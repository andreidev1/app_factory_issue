from functools import wraps
from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restx import Api, Resource, fields, marshal_with


from db import db


def create_app():


    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():

        @app.route('/')
        def index():
            return 'hello world'
    
    return app


