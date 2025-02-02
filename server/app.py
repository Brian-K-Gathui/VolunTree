#!/usr/bin/env python3

# ===============================
#        FLASK APPLICATION
# ===============================

# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

# Local imports
from config import app, db
from routes import register_routes

# ===============================
#       FLASK INITIALIZATION
# ===============================
CORS(app)  # Enable Cross-Origin Resource Sharing
api = Api(app)  # Initialize Flask-RESTful API
Migrate(app, db)  # Enable database migrations

# Register API Routes
register_routes(api)

# ===============================
#       ROOT ENDPOINT
# ===============================
@app.route('/')
def index():
    return "<h1>VolunTree API Server is Running! 🌱</h1>\n"

# ===============================
#       RUN THE APPLICATION
# ===============================
if __name__ == '__main__':
    print("\n🚀 VolunTree API is starting...")
    print("_____________________________________________\n")
    app.run(port=5555, debug=True)
