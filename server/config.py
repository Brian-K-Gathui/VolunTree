#!/usr/bin/env python3

# ===============================
#        CONFIGURATION FILE
# ===============================

# Standard library imports
import sys
import subprocess

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


# ==============================
# DATABASE MIGRATION HANDLER
# ==============================
def run_command(command, success_msg, error_msg):
    """Runs a shell command and handles success/failure messages."""
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ {success_msg}")
        print("_____________________________________________\n")  # Divider after success
    except subprocess.CalledProcessError as e:
        print(f"❌ {error_msg}\nError details: {e}")
        sys.exit(1)


# -------------------------------
# RUN MIGRATION COMMANDS (Only run if not already done)
# -------------------------------
if __name__ == "__main__":
    print("📂 Initializing database migrations...")
    print("_____________________________________________\n")

    # Run flask db init (only if migrations directory doesn't exist)
    if subprocess.call("flask db init", shell=True) == 0:
        print("✅ Migrations directory successfully created! 🚀")
        print("_____________________________________________\n")

    # Run flask db migrate (only if migrations need to be generated)
    if subprocess.call('flask db migrate -m "Initial migration"', shell=True) == 0:
        print("✅ Migration script successfully generated! 📝")
        print("_____________________________________________\n")

    # Run flask db upgrade (only if database schema needs to be updated)
    if subprocess.call("flask db upgrade", shell=True) == 0:
        print("✅ Database schema successfully applied! 🎉")
        print("_____________________________________________\n")

    print("\n🎯 All migration steps completed successfully!")
    print("🚀 You can now run the Flask server using: `flask run`")
    print("_____________________________________________\n")
