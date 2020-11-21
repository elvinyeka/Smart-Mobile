from flask import render_template,session,request,redirect, flash, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

from Smart import app, db, bcrypt
from .forms import  RegistrationForm, LoginForm
from .models import  User


@app.route('/')
def index():
    return render_template('index.html', title='home')

@app.route('/admin')
def admin():
    return render_template('admin/index.html', title='Admin Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)

        user = User(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.name.data} Qeydiyyat uğurlu oldu', 'success')
        return redirect(url_for('admin'))
    return render_template('admin/register.html', form=form,title='Registeration Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Xoş gəldiniz {form.email.data} Girişiniz uğurlu oldu.', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Şifrə səhvdir. Yenidən cəhd edin', 'danger')

    return render_template('admin/login.html',form=form, title='login')

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

@app.route('/compare')
def compare():
    return render_template('compare.html', title='compare')



    
    

@app.route('/single-product')
def single_product():
    return render_template('single-product.html',title='product')

@app.route('/brand-product')
def brand_product():
    return render_template('brand-product.html',title='brand')