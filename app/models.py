from . import db
from datetime import datetime


class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    photo_path = db.Column(db.String)
    category = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def save_photo(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_photos(cls, category):
        photos = Photo.query.filter_by(category=category).all()
        return photos

    @classmethod
    def get_photo(cls, id):
        photo = Photo.query.filter_by(id=id).first()
        return photo
