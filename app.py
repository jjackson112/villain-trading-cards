from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

# Initialize the Flask application
app = Flask(__name__)

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



@app.route("/")
def hello_world():
  return render_template("villain.html")

# Run the flask server
if __name__ == "__main__":
    app.run()