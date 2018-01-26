from flask import jsonify
import exchange.utils.model_utils
import json


class User(exchange.utils.model_utils.Model):
    permitted_fields = ['id', 'name', 'deleted']
    usable_permitted_fields = ['name']

    def __init__(self, ide, nome):
        self.id = ide
        self.name = nome
        self.deleted = False

    def delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False


DATA = exchange.utils.model_utils.ModelList()

for j, i in enumerate(['Ernesto','Arnaldo','Fred']):
    DATA.append(User(j+1, i))

# Precisa achar um jeito de implementar o json_utils
# Precisa ajeitar o controller do user e o __init__ para o método DELETE
