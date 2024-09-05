from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Student
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")
@views.route('/courses')
def courses():
    return render_template("courses.html")
@views.route('/contact')
def contact():
    return render_template("contact.html")
@views.route('/about')
def about():
    return render_template("about.html")


