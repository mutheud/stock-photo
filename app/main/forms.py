from flask_wtf import FlaskForm
from wtforms.validators import Required


class SubmitPhoto(FlaskForm):
    description = TextArea('Text', Validators=[Required()])
    category = SelectedField('Type', choices=[('place', 'Place Photos'), ('people', 'People Photos'), ('work', 'Work Photos'), ('food', 'Food Photos'), ('activate', 'Active Photos')], validators=[Required()])
    submit = SubmitField('Submit')
