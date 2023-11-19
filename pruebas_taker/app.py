import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from view import HealthCheck, PruebaInit, PruebaNext, PruebaDone

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True

if 'USERS_PATH' in os.environ:
    #app.config['USERS']  = str(os.environ.get("USERS_PATH")) +'/users/me'
    app.config['CACHE_HOST']  = str(os.environ.get("CACHE_PATH"))
    app.config['CACHE_PORT']  = str(os.environ.get("CACHE_PORT"))
    app.config['CANDIDATOS_QUERY'] = str(os.environ.get("CANDIDATOS_PATH"))
    app.config['PRUEBAS_QUERY'] = str(os.environ.get("PRUEBAS_PATH"))
    app.config['CANDIDATOS_PRUEBAS'] = str(os.environ.get("CANDIDATOS_PRUEBAS_PATH"))
    print("prod env-var")
    print("cache: ", app.config['CACHE_HOST'], app.config['CACHE_PORT'] )
    print("cands_url: ", app.config['CANDIDATOS_QUERY'])
    print("tests_url: ", app.config['PRUEBAS_QUERY'])
    print("testc_url: ", app.config['CANDIDATOS_PRUEBAS'])
else:
    app.config['CACHE_HOST']  = 'localhost'
    app.config['CACHE_PORT']  = 6379
    app.config['CANDIDATOS_QUERY'] = 'http://localhost:80/candidates-qry'
    app.config['PRUEBAS_QUERY'] = 'http://localhost:80/pruebas-qry'
    app.config['CANDIDATOS_PRUEBAS'] = 'http://localhost:80/candidatesTest'    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pruebas-taker.db'
    app.config['TESTING'] = True
    print("test env-var")
    print("cache: ", app.config['CACHE_HOST'], app.config['CACHE_PORT'] )
    print("cands_url: ", app.config['CANDIDATOS_QUERY'])
    print("tests_url: ", app.config['PRUEBAS_QUERY'])
    print("testc_url: ", app.config['CANDIDATOS_PRUEBAS'])    
    print("test: ", app.config['SQLALCHEMY_DATABASE_URI'])

app_context = app.app_context()
app_context.push()

cors = CORS(app)
api = Api(app)

api.add_resource(PruebaInit, '/tests-taker/init/<candidatoId>/<pruebaId>')
api.add_resource(PruebaNext, '/tests-taker/next/<candidatoId>/<pruebaId>')
api.add_resource(PruebaDone, '/tests-taker/done/<candidatoId>/<pruebaId>')
api.add_resource(HealthCheck, '/tests-taker/ping')  
