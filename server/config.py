#!/usr/bin/env python3

# ===============================
#        CONFIGURATION FILE
# ===============================

# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# -------------------------------
# FLASK APPLICATION SETUP
# -------------------------------
app = Flask(__name__)

# -------------------------------
# DATABASE CONFIGURATION
# -------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voluntree.db'  # SQLite database for VolunTree
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Secret key for session handling
app.json.compact = False  # Ensures better JSON formatting

# -------------------------------
# DATABASE INITIALIZATION
# -------------------------------
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)  # Create a SQLAlchemy database instance
migrate = Migrate(app, db)  # Initialize migration support
db.init_app(app)  # Bind SQLAlchemy to the Flask app

# -------------------------------
# API & CORS SETUP
# -------------------------------
api = Api(app)  # Initialize RESTful API
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for frontend communication

print("\n✅ Flask app configured successfully!")
print("🚀 Database connected to 'voluntree.db'")
print("_____________________________________________\n")
