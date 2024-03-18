from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frc_data.db'  # SQLite database URI
db = SQLAlchemy(app)

# Define models corresponding to the tables in your database
class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, unique=True)
    description = db.Column(db.Text)

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, db.ForeignKey('year.year'))
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100))

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))
    match_number = db.Column(db.Integer)

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    score = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    awards = db.Column(db.String(100))

# Wrap database operations inside a Flask application context
with app.app_context():
    # Query the data
    all_competitions = Competition.query.all()
    for competition in all_competitions:
        print(f"Competition: {competition.name}, Location: {competition.location}, Year: {competition.year}")

    # You can query other tables similarly to retrieve and view the data
