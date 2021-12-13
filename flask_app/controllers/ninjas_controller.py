from flask_app import app  
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/create', methods=['POST'])
def create_new_ninja():
    new_ninja = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.add_new_ninja(new_ninja)
    return redirect('/dojos')

@app.route('/ninjas/add')
def new_ninja():
    dojos = Dojo.get_dojo_list()
    return render_template('/ninjas.html', dojos=dojos)