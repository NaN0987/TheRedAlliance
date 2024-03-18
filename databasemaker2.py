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
    
    # Define a one-to-many relationship with Match
    matches = db.relationship('Match', backref='competition', lazy=True)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))
    match_number = db.Column(db.Integer)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100))

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    score = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    awards = db.Column(db.String(100))

# Create the database and apply the models
with app.app_context():
        # Create the database and apply the models
    # Assume the team number is 1234
    team = Team.query.filter_by(number=1234).first()
    if team:
        competition_2024 = Competition.query.filter_by(year=2024).first()
        if competition_2024:
            # Assuming the team participated in all matches of the competition
            matches = Match.query.filter_by(competition_id=competition_2024.id).all()
            for match in matches:
                # Assuming the team got first place in each match
                performance = Performance(match_id=match.id, team_id=team.id, score=40, ranking=1, awards='First Place')
                db.session.add(performance)
            db.session.commit()
        else:
            print("Competition for 2024 does not exist.")
    else:
        print("Team with number 1234 does not exist.")
