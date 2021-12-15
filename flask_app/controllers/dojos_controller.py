from flask_app import app  
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo



@app.route('/')
def to_dojo_home():
    return redirect('/dojos')

@app.route('/dojos')
def dojo_home():
    dojos = Dojo.get_dojo_list()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/<int:id>/show')
def show_ninjas(id):
    data = {'id':id}    
    dojo = Dojo.view_given_dojo(data)
    print(dojo)
    return render_template('dojos_show.html', dojo = dojo)

@app.route('/dojo/create', methods = ['POST'])
def create_dojo():
    data = {'dojo_name':request.form['dojo_name']}
    print("****************************",data)
    dojo = Dojo.create_new_dojo(data)
    print("*****************************",dojo)
    return redirect(f"/dojos/{dojo}/show")