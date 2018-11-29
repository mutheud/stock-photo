from flask import render_template, request, redirect, url_for, abort
from ..models import Photo
from .forms import SubmitPhoto
from . import main
import datetime


@main.route('/')
def index():

    '''
        View Root page function that returns the index page and it's data
    '''
    title = 'POC Stock Photo'
    place_photos = Photo.get_photos('place')
    people_photos = Photo.get_photos('people')
    work_photos = Photo.get_photos('work')
    food_photos = Photo.get_photos('food')
    active_photos = Photo.get_photos('active')
    return render_template('index.html', title=title, place=place_photos, people=people_photos, work=work_photos, food=food_photos, active=active_photos)


@main.route('/photo/new', methods=['GET', 'POST'])
def new_photo():
    submit_form = SubmitPhoto()
    if submit_form.validate_on_submit():

        description = submit_form.description.data
        category = submit_form.category.data

        # Updated Photo instance
        new_photo = Photo(description=description, category=category)

        # Save Photo Method
        new_photo.save_photo()
        return redirect(url_for('.index'))
    title = 'New Photo'
    return render_template('submit_photo.html', title=title, submit_form=submit_form)



@main.route('/photos/active')
def active():
    photos = Photo.get_photos('active')
    return render_template("active.html", title= 'Active', photos=photos)

@main.route('/photos/food')
def food():
    photos = Photo.get_photos('food')
    return render_template("food.html", title= 'Food', photos=photos)

@main.route('/photos/people')
def people():
    photos = Photo.get_photos('people')
    return render_template("people.html", title= 'People', photos=photos)

@main.route('/photos/place')
def place():
    photos = Photo.get_photos('place')
    return render_template("place.html", title= 'Place', photos=photos)

@main.route('/photo/work')
def work():
    photos = Photo.get_photos('work')
    return render_template("work.html", title= 'Work', photos=photos)
