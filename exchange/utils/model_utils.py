from flask import jsonify
import exchange.user.model


class Model(object):
    permitted_fields = []

    def to_json(self):
        return jsonify(self.to_dict())

    def to_dict(self):
        return self.__dict__

    @classmethod
    def check_permitted(cls, data):
        model_fields = {}
        for key, value in data.items():
            if key in cls.permitted_fields:
                model_fields[key] = value
            return model_fields


class ModelList(list):

    def to_json(self):
        tmp = []
        for i in self:
            tmp.append(i.to_dict())
        return jsonify(tmp)
