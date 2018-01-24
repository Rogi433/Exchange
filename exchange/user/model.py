from flask import jsonify
import json


class Model(object):
    def to_json(self):
        return self.__dict__


class ModelList(list):
    def to_json(self):
        tmp = []
        for i in self:
            tmp.append(i.to_json())
        return jsonify(tmp)


class User(Model):
    permitted_fields = ['id', 'name']

    def __init__(self, ide, nome):
        self.id = ide
        self.name = nome
        self.deleted = False

    def delete(self):
        self.deleted = True

# Essa função deve ir pra classe Model!
    def check_permitted(self, data):
        clean_data = {}
        for key, value in data.items():
            if key in User.permitted_fields:
                clean_data[key] = value
        return clean_data


# Precisa achar um jeito de implementar o json_utils
# Precisa gerar um modelo genérico em model_utils
# Precisa ajeitar o controller do user e o __init__
