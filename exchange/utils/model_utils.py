from flask import jsonify


class Model(object):
    def to_json(self):
        return jsonify(self.__dict__)

    def check_permitted(self, data, permitted_fields):
        for key, value in data.items():
            if key not in permitted_fields:
                return False
        return True


class ModelList(list):
    def to_json(self):
        tmp = []
        for i in self:
            tmp.append(i.to_json())
        return jsonify(tmp)