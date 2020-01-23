from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Predictions(FlaskForm):
    prediction = StringField('Prediction', validators=[DataRequired()])
    submit = SubmitField('Submit')

# title = StringField('Title', validators=[DataRequired()])
# year = StringField('Year', validators=[DataRequired()])