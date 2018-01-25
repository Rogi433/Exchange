from flask import jsonify
import exchange.utils.model_utils
import json


class User(exchange.utils.model_utils.Model):
    permitted_fields = ['name']

    def __init__(self, ide, nome):
        self.id = ide
        self.name = nome
        self.deleted = False

    def delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False


DATA = exchange.utils.model_utils.ModelList()
u1 = User(1, 'Ernesto')
u2 = User(2, 'Arnaldo')
u3 = User(3, 'Fred')

DATA.append(u1)
DATA.append(u2)
DATA.append(u3)

# Precisa achar um jeito de implementar o json_utils
# Precisa ajeitar o controller do user e o __init__ para o método DELETE
