from flask_wtf import form
from wtforms import TextField
from wtforms.validators import DataRequired, Length
"""
class AcountForm(form):
   title = TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(),Length(max=140)]
    )
"""