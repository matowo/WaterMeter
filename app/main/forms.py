from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length, Regexp
from flask_babel import _, lazy_gettext as _l
from app.models import User
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username'))


class PhoneForm(FlaskForm):
    phone = StringField(_('PHONE'), validators=[DataRequired(), Regexp('[0-9]')],
                               render_kw={"placeholder": "Phone Number "}
                               )

    submit = SubmitField(_l('Update Phone'))


class BillingAddressForm(FlaskForm):
    address_line = TextAreaField(_('Address Line 1*'), validators=[DataRequired()], render_kw={'placeholder':"Address Line 1"})
    address_line_1 = TextAreaField(_('Address Line 2'), validators=[DataRequired()], render_kw={'placeholder': "Address Line 2"})
    accept = SubmitField(_l('Accept Changes'))



class EditBillingAddressForm(FlaskForm):
    address_line = TextAreaField(_('Address Line 1*'), validators=[DataRequired()],
                               render_kw={'placeholder': "Address Line 1"})
    address_line_1 = TextAreaField(_('Address Line 2'), validators=[DataRequired()],
                                 render_kw={'placeholder': "Address Line 2"})

    accept = SubmitField(_l('Accept Changes'))
