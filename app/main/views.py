from flask import render_template, request, redirect, url_for, abort
from ..models import 
from .forms import SubmitPhoto
from . import main
import datetime

@main.route('/')
def index():
    return render_template('index.html')


@main.route('submitphoto')
def submit_photo():
    return render_template ('submit_photo.html')