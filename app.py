from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask("app")

# set up SQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"
db = SQLAlchemy(app)

# organize SQL database
class Villain (db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(250), unique=True, nullable=False)
  interests = db.Column(db.String(250), unique=False, nullable=False)
  url = db.Column(db.String(250), nullable=False)
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Function to take self as an argument, prints the villain's name if the database is queried
def __repr__ (self):
  return "<Villain "+ self.name + ">"

# connect sql database to web app
with app.app_context():
  db.create_all()
  db.session.commit()

@app.route("/")
def villains_cards():
  return render_template("villain.html", villains=Villain.query.all())

# Add a villain to database
# errors handles if the user doesn't fill out required fields
@app.route("/add", methods=["GET"])
def add_villain():
  return render_template("addvillain.html", errors=[])

# Delete a villain from database
@app.route("/delete", methods=["GET"])
def delete_villain():
  return render_template("deleteVillain.html", errors = [])

# POST method to add villain
# errors alerts users if they don't submit all required fields
@app.route("/addVillain", methods=["POST"])
def add_user():
  errors = []
# get new villain's name
  name = request.form.get("name")
  if not name:
    errors.append("Oops! Looks like you forgot a name!")
  description = request.form.get("description")
  if not description:
    errors.append("Oops! Looks like you forgot a description!")
    interests = request.form.get("interests")
  if not interests:
   errors.append("Oops! Looks like you forgot some interests!")
  url = request.form.get("url")
  if not url:
    errors.append("Oops! Looks like you forgot an image!")

# query villain database
  villain = Villain.query.filter_by(name=name).first()
  if villain:
    errors.append("Oops! A villain with that name already exists!")

  if errors:
    render_template("addvillain.html", errors=errors)
  else:
    new_villain = Villain(name=name, description=description, interests=interests, url=url)
    db.session.add(new_villain)
    db.session.commit()
  return render_template("villain.html", villains=Villain.query.all())

# POST method to delete villain
@app.route("/deleteVillain", methods=["POST"])
def delete_user():
	name = request.form.get("name")
	villain = Villain.query.filter_by(name=name).first()
	if villain:
		db.session.delete(villain)
		db.session.commit()
		return render_template("villain.html", villains=Villain.query.all())
	else:
		return render_template("deletevillain.html", errors=["Oops! That villain doesn't exist!"])

# Run the flask server
app.run(host="0.0.0.0", port=8080)