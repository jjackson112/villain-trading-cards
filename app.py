from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime

# Initialize the Flask application
app = Flask("app")

# Configure location of new database 
# db connects to the toolkit to Flask project referred to as app which is passed as an argument
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"
db = SQLAlchemy(app)

# create a class to pass db.model as an argument - database model
# id data type is set to integer and the primary key attribute is set to true to be unique
class Villain (db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name= db.Column(db.String(80), unique = True, nullable = False)
  description = db.Column(db.String(250), nullable = False)
  interests = db.Column(db.String(250), nullable = False)
  url = db.Column(db.String(250), nullable = False)
  date_added = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

# define a function that takes self as an argument
def __repr__(self):
   return "<Villain " + self.name + ">"

# connect database to app
with app.app_context():
  db.create_all()
  db.session.commit()

@app.route("/")
def villain_cards():
  return render_template("villain.html")

@app.route("/add", methods=["GET"])
def add_villain():
   return render_template("addvillain.html", errors=[])

@app.route("/addVillain", methods=["POST"])
def add_user():
  # errors array will alert the user if they don't submit all required fields
  errors = []
  name = request.form.get("name")
    if not name:
      errors.append("Oops! Looks like you forgot a name!")
  description = request.form.get("description")
    if not description:
      errors.append("Oops! Looks like you need a description!")
  interests = request.form.get("interests")
    if not interests:
      errors.append("Oops! You need to add some interests!")
  url = request.form.get("url")
    if not url:
      errors.append("Oops! Looks like you forgot an image!")
   return render_template()

# Run the flask server
if __name__ == "__main__":
    app.run()