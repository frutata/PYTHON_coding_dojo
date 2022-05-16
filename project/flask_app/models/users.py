from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

from flask import flash

import re

EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User:
    db = 'val_guide_schema'
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#=======================
# STATIC methods
#=======================

    @staticmethod
    def validate_register(form_data):
        is_valid = True

        if len(form_data['username']) < 3:
            flash('*Username name MUST be at least 3 characters long!')
            is_valid = False

        if len(form_data['email']) < 1:
            flash('*Email MUST be present!')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']):
            flash('*PLEASE enter a valid email!')
            is_valid = False

        if len(form_data['password']) < 8:
            flash('*Password MUST be at least 8 characters long!')
            is_valid = False
        if form_data['password'] != form_data['password_conf']:
            flash('*Password and Confirmation MUST match!')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(form_data):

        is_valid = True

        user_in_db = User.get_by_username(form_data)
        # user is not registered in the db
        if not user_in_db:
            flash("Invalid Username/Password")
            is_valid = False

        elif not bcrypt.check_password_hash(user_in_db.password, form_data['password']):
            # if we get False after checking the password
            flash("Invalid Username/Password")
            is_valid = False

        return is_valid

#=======================
# CLASS methods
#=======================

    @classmethod
    def register_user(cls, data):
        query = ' INSERT INTO users (username, email, password, created_at) VALUES (%(username)s, %(email)s, %(password)s, NOW());'
        result = connectToMySQL(cls.db).query_db(query, data)
        return result


    @classmethod
    def get_by_username(cls,data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
