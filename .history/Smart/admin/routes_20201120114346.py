from flask import render_template,session,request,redirect, flash, url_for
from Smart import app,db


@app.route('/')
def index():
    return render_template('index.html', title='home')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    return render_template('register.html',title='Register User')


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