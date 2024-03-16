from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'  # SQLite database URI
db = SQLAlchemy(app)

print(db)

# Create the database and apply the model



