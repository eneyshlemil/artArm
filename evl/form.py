from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class LoadFileForm(FlaskForm):
    file = FileField('Загрузите файл', validators=[FileAllowed(['pdf'])])
    submit = SubmitField('Получить json')