#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from config import app, db
from routes import register_routes

CORS(app)
api = Api(app)
Migrate(app, db)

register_routes(api)

@app.route('/')
def index():
    return "<h1>VolunTree API Server is Running! 🌱</h1>\n"

if __name__ == '__main__':
    print("\n🚀 VolunTree API is starting...")
    print("_____________________________________________\n")
    app.run(port=5555, debug=True)
