from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.ninjas = []

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

    @classmethod
    def view_given_dojo(Dojo, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = (%(id)s)"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        # print("**********************************", results)
        dojo_location = results[0]
        new_dojo = Dojo(dojo_location)
        for row in results:
            new_dojo.ninjas.append(Ninja(row))
        
        print("***********************************", new_dojo)
        return new_dojo