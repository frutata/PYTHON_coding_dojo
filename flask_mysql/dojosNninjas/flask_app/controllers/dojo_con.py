from flask import redirect, render_template, request

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# ========================
# Default routes
# ========================

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

# ========================
# Editing routes
# ========================

@app.route('/dojos/create', methods=['POST'])
def create():
    print("test========================")
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all_dojos()
    # print(dojos)
    return render_template('ninjas.html', dojos = dojos)

@app.route('/ninjas/create', methods=['post'])
def newNinja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"],
    }

    Ninja.save(data)

    return redirect(f"/dojos/{data['dojo_id']}")

# ========================
# Other routes
# ========================

@app.route('/dojos/<int:id>')
def show_dojo_ninjas(id):
    data = {
        "id" : id
    }
    dojo = Dojo.get_one(data)
    return render_template('show.html', dojo = dojo)