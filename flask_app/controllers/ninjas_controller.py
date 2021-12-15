from flask_app import app  
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja_application():
    dojos = Dojo.get_dojo_list()
    
    return render_template('ninjas.html', dojos = dojos)

@app.route('/ninjas/add', methods = ['POST'])
def new_ninja():
    print("**************************")
    print(request.form)
    added_ninja = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_location_id']
    }
    Ninja.add_new_ninja(added_ninja)
    return redirect(f"/dojos/{added_ninja['dojo_id']}/show")