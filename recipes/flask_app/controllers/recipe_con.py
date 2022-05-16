from flask_app import app

from flask import render_template, request, redirect, flash, session

from flask_app.models.recipe import Recipe
from flask_app.models.user import User

#==========================
# Creation routes
#==========================

@app.route('/create')
def create():

    if 'user_id' not in session:
        flash('*PLEASE login or register before proceeding')
        return redirect('/')
    
    query_data = {
        'user_id' : session['user_id']
    }

    user = User.get_by_id(query_data)

    return render_template('create_recipe.html', user = user)

@app.route('/create/recipe', methods=['post'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/create')

    query_data_recipe = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instruction' : request.form['instruction'],
        'date_made_on' : request.form['date_made_on'],
        'under_30_min' : request.form['under_30_min'],
        'user_id' : session['user_id']
    }

    Recipe.new_recipe(query_data_recipe)

    return redirect('/dashboard')

#==========================
# Show routes
#==========================

@app.route('/recipe/<int:id>')
def recipe(id):

    if 'user_id' not in session:
        flash('*PLEASE login or register before proceeding')
        return redirect('/')

    data = {
        'id' : id
    }

    recipe = Recipe.show_recipe(data)

    query_data = {
        'user_id' : session['user_id']
    }

    user = User.get_by_id(query_data)

    return render_template('recipe.html', recipe = recipe, user = user)

@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):

    data = {
        'id' : id
    }

    Recipe.delete_recipe(data)

    return redirect('/dashboard')

#==========================
# Edit routes
#==========================

@app.route('/edit/<int:id>')
def edit_recipe(id):

    if 'user_id' not in session:
        flash('*PLEASE login or register before proceeding')
        return redirect('/')

    data = {
        'id' : id
    }

    recipe = Recipe.show_recipe(data)

    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/edit/recipe/<int:id>', methods=['post'])
def edit_recipe_data(id):

    if not Recipe.validate_recipe(request.form):
        return redirect(f'/edit/{id}')

    query_data_recipe = {
        'id' : request.form['id'],
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instruction' : request.form['instruction'],
        'date_made_on' : request.form['date_made_on'],
        'under_30_min' : request.form['under_30_min'],
        'user_id' : session['user_id']
    }

    Recipe.edit_recipe(query_data_recipe)

    return redirect('/dashboard')