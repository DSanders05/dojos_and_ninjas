from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']

    @classmethod
    def get_dojo_list(Dojo):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for row in results:
            dojos.append(Dojo(row))
        return dojos

    @classmethod
    def create_new_dojo(Dojo, data):
        query = "INSERT INTO dojos (dojo_name) VALUES (%(dojo_name)s)"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result