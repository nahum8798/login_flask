from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import User, Product
from app.forms import LoginForm, RegistrationForm, AddProduct
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint('main', __name__)


"""
User routes
"""

@bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login succesful', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your email and/ or password','danger')

    return render_template('login.html', form=form)


@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            flash('Password must match', 'danger')
            return redirect(url_for('main.register'))
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'succes')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('main.index'))


"""
Product routes
"""

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def addProduct():

    form = AddProduct()

    if form.validate_on_submit():
        product = Product(
            name_product = form.name_product.data,
            price_product = form.price_product.data,
            stock_product = form.stock_product.data,
            id_user = current_user.id

        )

        db.session.add(product)
        db.session.commit()
        flash('Producto agregado exitosamente', 'succes')
        return redirect(url_for('main.index'))

    return render_template('addProduct.html', form=form)


@bp.route('/')
def index():
    return render_template('index.html')

