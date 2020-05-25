import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from flask import render_template

from flask_cors import CORS
# from config import password


#################################################
# Database Setup
#################################################

engine = create_engine("postgresql://postgres:postgres@localhost:5432/puntpasspredict")


conn = engine.connect()

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
NFL = Base.classes.NFL_Plays
# Team = Base.classes.Team_ID

# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

# Flask Routes
#################################################

# Route to render index.html
# @app.route("/")
# def home():
#     # Return template and data
#     return render_template("index.html")

@app.route("/api/v1.0/NFL_Plays")   
def plays():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query play data
    play_data = session.query(
        NFL.home_team,
        NFL.away_team,
        NFL.posteam,
        NFL.game_date,
        # NFL.yardline_100,
        # NFL.quarter_seconds_remaining,
        NFL.qtr,
        NFL.down,
        NFL.ydstogo,
        NFL.yrdln,
        NFL.ydsnet,
        NFL.desc,
        NFL.play_type,
        NFL.total_home_score,
        NFL.total_away_score, 
        NFL.team_id.all()

    session.close()

    # Create a dictionary to hold play history data
    play_history = []
    for home_team, away_team, posteam, yardline_100, quarter_seconds_remaining, qtr, down, ydstogo, yrdln, desc, play_type, total_home_score, total_away_score, team_id in play_data:
        play_dict = {}
        play_dict["home_team"] = home_team
        play_dict["away_team"] = away_team
        play_dict["posteam"] = posteam
        play_dict["yardline_100"] = yardline_100
        play_dict["quarter_seconds_remaining"] = quarter_seconds_remaining
        play_dict["qtr"] = qtr
        play_dict["down"] = down
        play_dict["ydstogo"] = ydstogo
        play_dict["yrdln"] = yrdln
        play_dict["desc"] = desc
        play_dict["play_type"] = play_type
        play_dict["total_home_score"] = total_home_score
        play_dict["total_away_score"] = total_away_score
        play_dict["team_id"] = team_id
        play_history.append(play_dict)

    return jsonify(play_history)

if __name__ == '__main__':
    app.run(debug=True)
