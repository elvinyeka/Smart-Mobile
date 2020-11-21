from flask import render_template,session,request,redirect, flash, redirect, url_for
from Smart import app,db




@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')


@app.route('/register')
def register():
    return render_template('admin/register.html', title = "Register user")