from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = ['updated_at']

        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for i in results:
            dojos.append(cls(i))
        return dojos

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at) VALUES (%(newDojo)s, NOW());'
        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)

        dojo = cls(result[0])

        for row in result:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'dojo_id': row['dojo_id'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # print(result)
        dojos = []

        for one_dojo in result:
            dojos.append(cls(one_dojo))
        # print(dojos)
        return dojos
