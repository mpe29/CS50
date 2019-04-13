#####################IMPORTS#######################
import csv
import os

from flask import Flask, render_template, request
from objects import *
from flask_sqlalchemy import SQLAlchemy

####################CONFIG#########################

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

####################IMPORT##########################

def main():
	db.create_all() #created all tables given classes provided in "Objects"
	csvfile = open("books.csv")
	reader = csv.reader(csvfile)
	next(csvfile) #this should skip the first line

	for isbn, title, author, year in reader:
		book = Book(isbn=isbn, title=title, author=author, year=year)
		db.session.add(book)
		print(f"Added {title} by {author}.")
	db.session.commit() #trying this not in the for loop as it was very slow innitially uploading 5000 books!

if __name__ == "__main__":
    with app.app_context():
        main()


