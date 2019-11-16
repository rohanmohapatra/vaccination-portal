from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {"origins": 'http://localhost:5000'}})

app.config["MONGO_URI"] = "mongodb://localhost:27017/cavach"
mongo = PyMongo(app)
