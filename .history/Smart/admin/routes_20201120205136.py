from flask import render_template,session,request,redirect, flash, url_for, flash

from Smart import app,db, bcrypt
from .forms import  RegistrationForm
from .models import  User


@app.route('/')
def index():
    return render_template('index.html', title='home')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)

        user = User(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password)
        db.session.add(user)
        flash(f'{form.name.data}Thanks for registering', 'success')
        return redirect(url_for('admin'))
    return render_template('admin/register.html', form=form,title='Registeration Page')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

@app.route('/compare')
def compare():
    return render_template('compare.html', title='compare')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html',title='login')

@app.route('/single-product')
def single_product():
    return render_template('single-product.html',title='product')

@app.route('/brand-product')
def brand_product():
    return render_template('brand-product.html',title='brand')