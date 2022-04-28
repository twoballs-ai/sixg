from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()


class ContactForm(FlaskForm):
    name = StringField('Имя : ', validators=[DataRequired('Имя не может быть пустым')])
    email = StringField('E-mail :', validators=[DataRequired('Email не может быть пустой'),Email('Пожалуйста, укажите действительный Email')])
    message = TextAreaField('Сообщение :', validators=[DataRequired('Введите ваше сообщение')])
    submit = SubmitField("Отправить")

