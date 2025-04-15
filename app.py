from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask("app")

# set up SQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"
db = SQLAlchemy(app)

# organize SQL database
class Villain (db.model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(250), unique=True, nullable=False)
  interests = db.Column(db.String(250), unique=False, nullable=False)
  url = db.Column(db.String(250), nullable=False)
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Function to take self as an argument, prints the villain's name if the database is queried
def __repr__ (self):
  return "<Villain "+ self.name + ">"

@app.route("/")
def hello_world():
  return render_template("villain.html")

# Run the flask server
app.run(host="0.0.0.0", port=8080)
