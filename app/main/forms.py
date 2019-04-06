from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
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


class PostBlog(FlaskForm):
    blog_title = StringField('Title')
    blog_cover = FileField('', validators=[FileRequired(),
                                                 FileAllowed(['jpg', 'png', 'gif', 'jpeg', 'exif', 'tiff', 'bmp',
                                                              'img'],
                                                             'Images Video Only')],
                                 render_kw={"placeholder": "Blog Cover"})
    body = CKEditorField('Blog post')
    submit = SubmitField('Submit')