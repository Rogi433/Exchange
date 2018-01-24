from flask import jsonify


class Model(object):
    def to_json(self):
        return self.__dict__

    def check_permitted(self, dict):
    # INCOMPLETA
        return dict


class ModelList(list):
    def to_json(self):
        tmp = []
        for i in self:
            tmp.append(i.to_json())
        return jsonify(tmp)