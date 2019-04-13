#####################IMPORTS########################

import os

from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, jsonify, request

from objects import *

import requests
import json

# Goodreads KEY = jzvKdHykLEpBlS4GhC8uw
# Goodreads SECRET = WeLIUIrhtBtWv65kJ2IjkBAdquwS2pMkXiDS99gVjo

######################CONFIG########################

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

# Check for environment variable
# Remember set environment variable using "export DATABASE_URL = postgres://xkslffelxynzbr:0996b5976cf55d6d5be6e041fdc30e85a47af7e87d09e3914170573d279d5407@ec2-54-225-242-183.compute-1.amazonaws.com:5432/d5614b9mik9vj9"
# That long string is the URI provided by Heroku 

# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")
# Configure session to use filesystem

#################CHEEKY_VARIABLES###################

# Goodreads API Key
KEY = "jzvKdHykLEpBlS4GhC8uw"

######################ROUTES########################

@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/books/")
def books():
	books = Book.query.all()
	return render_template("books.html", books=books)

@app.route("/books/<int:book_id>")
def review(book_id):
    """List details about a single book under review."""
    # next Step here is to enable a user to add a review
    # this step will likely need a "current_rating" and "updated_rating"

    # Make sure Book exists.
    book = Book.query.get(book_id)
    if book is None:
        return render_template("error.html", message="No such book.")

    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": KEY, "isbns": book.isbn})
    data=res.json()

    avg_rating = data['books'][0]['average_rating']
    rating_count = data['books'][0]['ratings_count']
    # reviews = review.book_id
    return render_template("reviews.html", book=book, rating=rating)

