from flask_app import app  
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos_home():
    dojos = Dojo.get_dojo_list()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojos/create', methods = ['POST'])
def add_new_dojo():
    new_dojo = {
        'dojo_name': request.form['dojo_name']
    }
    Dojo.create_new_dojo(new_dojo)
    return redirect('/dojos')