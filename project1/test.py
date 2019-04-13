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

####################ADD##########################

def main():
	books = Book.query.get(5002)
	# print(f"Added {book.title()} by {book.author()}.")
	# db.session.commit()
	books.title="The One Poop to Rule Them All!"
	print(books.title)
	db.session.commit()



if __name__ == "__main__":
    with app.app_context():
        main()
