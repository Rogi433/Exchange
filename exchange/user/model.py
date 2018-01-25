from flask import jsonify
import exchange.utils.model_utils
import json


class User(exchange.utils.model_utils.Model):
    permitted_fields = ['id', 'name']

    def __init__(self, ide, nome):
        self.id = ide
        self.name = nome
        self.deleted = False

    def delete(self):
        self.deleted = True


# Precisa achar um jeito de implementar o json_utils
# Precisa gerar um modelo genérico em model_utils
# Precisa ajeitar o controller do user e o __init__
