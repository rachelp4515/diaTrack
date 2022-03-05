from time import time
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField,TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from bs_track.models import ACTIONTYPES, Bloodsugar, Action


class BloodsugarForm(FlaskForm):
    bs = StringField(
        'Current Blood Sugar', validators=[DataRequired(), Length(min=2, max=3)]
    )
    time = StringField('Time - please format 24hour.minutes', validators=[DataRequired(), Length(min=2, max=6)])
    action = SelectField('Action', choices= ACTIONTYPES.choices())
    submit = SubmitField('Submit')


class ActionForm(FlaskForm):
    time = StringField('Time - please format 24hour.minutes', validators=[DataRequired(), Length(min=2, max=6)])
    act_type = SelectField('Action', choices= ACTIONTYPES.choices())
    notes = TextAreaField(
        'Notes', validators=[DataRequired(), Length(min=0, max=180)]
    )
    submit = SubmitField('Submit')

