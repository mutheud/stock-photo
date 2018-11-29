from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class SubmitPhoto(FlaskForm):
    description = TextAreaField('Text', validators=[Required()])
    category = SelectField('Type', choices=[('place', 'Place'), ('people', 'People'), ('work', 'Work'), ('food', 'Food'),
     ('active', 'Active')] )
    submit = SubmitField('Submit')
