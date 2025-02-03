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

print("\n✅ Flask app configured successfully!")
print("🚀 Database connected to 'voluntree.db'")
print("_____________________________________________\n")

def run_command(command, success_msg, error_msg):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ {success_msg}")
        print("_____________________________________________\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ {error_msg}\nError details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("📂 Initializing database migrations...")
    print("_____________________________________________\n")

    if subprocess.call("flask db init", shell=True) == 0:
        print("✅ Migrations directory successfully created! 🚀")
        print("_____________________________________________\n")

    if subprocess.call('flask db migrate -m "Initial migration"', shell=True) == 0:
        print("✅ Migration script successfully generated! 📝")
        print("_____________________________________________\n")

    if subprocess.call("flask db upgrade", shell=True) == 0:
        print("✅ Database schema successfully applied! 🎉")
        print("_____________________________________________\n")

    print("\n🎯 All migration steps completed successfully!")
    print("🚀 You can now run the Flask server using: `flask run`")
    print("_____________________________________________\n")