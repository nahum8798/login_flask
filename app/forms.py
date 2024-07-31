from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,IntegerField ,SubmitField
from wtforms.validators import DataRequired, Email, Length

"""
Definimos una clase por cada formulario:

"""


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


"""
Products forms
"""

class AddProduct(FlaskForm):
    name_product = StringField('Producto', validators=[DataRequired()])
    price_product = IntegerField('Precio', validators=[DataRequired()])
    stock_product = IntegerField('Stock', validators=[DataRequired()])
    submit = SubmitField('Agregar producto')