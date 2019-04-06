from flask_wtf import FlaskForm
import pycountry
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Regexp
from flask_babel import _, lazy_gettext as _l
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()],
                           render_kw={"placeholder": "Username"}
                           )
    password = PasswordField(_l('Password'), validators=[DataRequired()],
                             render_kw={"placeholder": "Password"}
                             )
    remember_me = BooleanField(_l('Keep Me Signed In'))
    submit = SubmitField(_l('Sign In'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField(_l('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    email = StringField(_l('Email'), validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    #phone = StringField(_l('Phone'), validators=[DataRequired(),], render_kw={"placeholder": "Phone number (255)"})
    password = PasswordField(_l('Password'), validators=[DataRequired()], render_kw={"placeholder": "Password"})
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password'),], render_kw={"placeholder": "Confirm Password"}
    )

    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different username'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different email address'))


class PhoneRegistrationField(FlaskForm):
    country = SelectField(_l(''))


    def __init__(self, *args, **kwargs):
        super(PhoneRegistrationField, self).__init__(*args, **kwargs)
        self.choices = [(country.alpha2, country.name) for country in pycountry.countries]

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField(_l('Request Password Reset'))

