from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash, request

class Recipe:
    db = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made_on = data['date_made_on']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#=======================
# STATIC methods
#=======================

    @staticmethod
    def validate_recipe(form_data):
        is_valid = True

        if len(form_data['name']) < 3:
            flash('*Name MUST be 3 characters long and present!')
            is_valid = False
        if len(form_data['description']) < 3:
            flash('*Description MUST be 3 characters long and present!')
            is_valid = False
        if len(form_data['instruction']) < 3:
            flash('*Instructions MUST be 3 characters long and present!')
            is_valid = False
        if len(form_data['date_made_on']) < 6:
            flash('*Date MUST be filled in!')
            is_valid = False
        if 'under_30_min' not in form_data:
            flash('*Under 30 minutes MUST be checked!')
            is_valid = False

        return is_valid

#=======================
# CLASS methods
#=======================

    @classmethod
    def new_recipe(cls, data):
        query = 'INSERT INTO recipes (name, description, instruction, date_made_on, under_30_min, created_at, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(date_made_on)s, %(under_30_min)s, NOW(), %(user_id)s)'
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_all_recipes(cls, data):
        query = 'SELECT * FROM recipes;'
        result = connectToMySQL(cls.db).query_db(query, data)
        recipes = []
        for i in result:
            recipes.append( cls(i) )
        return recipes

    @classmethod
    def show_recipe(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def edit_recipe(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_made_on = %(date_made_on)s, under_30_min = %(under_30_min)s, updated_at = NOW() WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return result