from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frc_data.db'  # SQLite database URI
db = SQLAlchemy(app)

# Define models corresponding to the tables in your database
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100))

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_number = db.Column(db.Integer)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    awards = db.Column(db.String(100))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))


# Create the database and apply the models
with app.app_context():
   
    @app.route('/edit_performance', methods=['GET', 'POST'])
    def edit_performance():
        if request.method == 'POST':
            team_number = request.form['team_number']
            match_number = request.form['match_number']
            score = request.form['score']
            ranking = request.form['ranking']
            awards = request.form['awards']

            # Query the team with the given team number
            team = Team.query.filter_by(number=team_number).first()
            if team:
                # Query the match with the given match number
                match = Match.query.filter_by(match_number=match_number).first()
                if match:
                    # Update or create the performance record for the team in the match
                    performance = Performance.query.filter_by(match_id=match.id, team_id=team.id).first()
                    if not performance:
                        performance = Performance(match_id=match.id, team_id=team.id)
                    performance.score = score
                    performance.ranking = ranking
                    performance.awards = awards
                    db.session.add(performance)
                    db.session.commit()
                    return 'Performance updated successfully.'
                else:
                    return 'Match does not exist.'
            else:
                return 'Team does not exist.'

        return render_template('addData.html')

    if __name__ == '__main__':
        app.run(debug=True)
