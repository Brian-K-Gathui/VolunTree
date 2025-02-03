#!/usr/bin/env python3

import sys
import subprocess

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voluntree.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'
app.json.compact = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
CORS(app)
print("\n_____________________________________________\n")
print("✅ Flask app configured successfully!")
print("🚀 Database connected to 'voluntree.db'")

def run_command(command, success_msg, error_msg):
    try:
        subprocess.run(command, shell=True, check=True)
        print("_____________________________________________\n")
        print(f"✅ {success_msg}")
        print("_____________________________________________\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ {error_msg}\nError details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("\n_____________________________________________\n")
    print("📂 Initializing database migrations...")
    print("_____________________________________________\n")

    run_command(
        "flask db init",
        "Migrations directory successfully created! 🚀",
        "Failed to initialize migrations directory."
    )

    run_command(
        'flask db migrate -m "Initial migration"',
        "Migration script successfully generated! 📝",
        "Failed to generate migration script."
    )

    run_command(
        "flask db upgrade",
        "Database schema successfully applied! 🎉",
        "Failed to apply database schema."
    )

    print("_____________________________________________\n")
    print("🎯 All migration steps completed successfully!")
    print("🚀 You can now run the Flask server using: `flask run`")
    print("_____________________________________________\n")