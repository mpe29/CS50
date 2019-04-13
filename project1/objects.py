import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#####################OBJECTS######################

class Book(db.Model):
	__tablename__ = "books"
	id = db.Column(db.Integer, primary_key=True)
	isbn = db.Column(db.String, nullable=False)
	title = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	year = db.Column(db.String, nullable=False)

	def add_review(self, rating, review):
		r = Review(rating=rating, review=review, book_id=self.id)


class Review(db.Model):
	__tablename__ = "reviews"
	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
	review = db.Column(db.String, nullable=True)
# May try Float after sorted with Integer
	rating = db.Column(db.Integer, nullable=False)

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)


#Author class is not essential but would be useful perhaps and can be added later
# class Author(db.Model):
# 	__tablename__ = "authors"
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String, nullable=False)
# 	book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
	