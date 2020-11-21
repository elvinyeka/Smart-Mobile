from flask import redirect, render_template, url_for, flash, request
from Smart import db, app
from .models import Brand, Category




@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'Brand "{getbrand}" Data Bazaya əlavə olundu.', 'success')
        return redirect(url_for('addbrand'))
        db.session.commit()
    return render_template('products/addbrand.html', brands = 'brands')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        flash(f'Kategoriya "{getcat}" Data Bazaya əlavə olundu.', 'success')
        return redirect(url_for('admin'))
        db.session.commit()
    return render_template('products/addbrand.html')