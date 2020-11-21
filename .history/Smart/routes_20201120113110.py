from flask import render_template,session,request,redirect, flash, url_for
from Smart import app,db
from Smart.forms import RegisterForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html', title='home')



@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

@app.route('/compare')
def compare():
    return render_template('compare.html', title='compare')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    return render_template('signup.html',title='signup')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html',title='login')

@app.route('/single-product')
def single_product():
    return render_template('single-product.html',title='product')

@app.route('/brand-product')
def brand_product():
    return render_template('brand-product.html',title='brand')