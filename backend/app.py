from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
\from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
CORS(app)

database_url = os.getenv('DATABASE_URL', 'postgresql://postgres:0613@localhost:5432/fragrance_finder')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from models import *
from routes import *

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)