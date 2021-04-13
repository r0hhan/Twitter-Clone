from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import IMAGES

class RegisterForm(FlaskForm):
	name = StringField('Full name', validators=[InputRequired('A full name is required.'), Length(max=100, message='Your name can\'t be more than 100 characters')])
	username = StringField('Username', validators=[InputRequired('A username is required.'), Length(max=30, message='Your username can\'t be more than 30 characters')])
	password = PasswordField('Password', validators=[InputRequired('A password is required!')])
	image = FileField(validators=[FileAllowed(IMAGES, message='Only images are accepted!')])

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired('A username is required.')])
	password = PasswordField('Password', validators=[InputRequired('A password is required.')])
	remember = BooleanField('Remember Me')

class TweetForm(FlaskForm):
	text = TextAreaField('Message', validators=[InputRequired('Enter your tweet...')])