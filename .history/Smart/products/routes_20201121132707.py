from flask import redirect, render_template, url_for, flash, request
from Smart import db, app
from .models import Brand, Category




@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
    return render_template('products/addbrand.html')