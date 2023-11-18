import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from view import HealthCheck, PruebaInit, PruebaNext, PruebaDone

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True

if 'USERS_PATH' in os.environ:
    #app.config['USERS']  = str(os.environ.get("USERS_PATH")) +'/users/me'
    app.config['CANDIDATOS_QUERY'] = str(os.environ.get("CANDIDATOS_QUERY_PATH"))
    app.config['PRUEBAS_QUERY'] = str(os.environ.get("PRUEBAS_QUERY_PATH"))
    app.config['CACHE_HOST']  = str(os.environ.get("CACHE_PATH"))
    app.config['CACHE_PORT']  = str(os.environ.get("CACHE_PORT"))
else:
    app.config['CANDIDATOS_QUERY'] = 'http://localhost:36961/candidates-query'
    app.config['PRUEBAS_QUERY'] = 'http://localhost:36962/pruebas-query'
    app.config['CACHE_HOST']  = 'localhost'
    app.config['CACHE_PORT']  = 6379

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pruebas-taker.db'
    app.config['TESTING'] = True
    print("test: ", app.config['SQLALCHEMY_DATABASE_URI'])

app_context = app.app_context()
app_context.push()

cors = CORS(app)
api = Api(app)

api.add_resource(PruebaInit, '/pruebas-taker/init/<string:candidatoId>/<string:pruebaId>')
api.add_resource(PruebaNext, '/pruebas-taker/next/<string:candidatoId>/<string:pruebaId>')
api.add_resource(PruebaDone, '/pruebas-taker/done/<string:candidatoId>/<string:pruebaId>')
api.add_resource(HealthCheck, '/pruebas-taker/ping')  
