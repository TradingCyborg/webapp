from flask import Flask
from flask_restx import Api,Resource

app=Flask(__name__)

app=Api(app,doc='/doc')


