from flask import current_app
import exchange.utils.json_utils as json_utils
import json


class Model(object):
    permitted_fields = []
    usable_permitted_fields = []

    def to_json(self):
        return current_app.response_class(
            json.dumps(self, default=json_utils.default_to_json, sort_keys=True, indent=4),
            mimetype=current_app.config['JSONIFY_MIMETYPE']
        )

    def to_dict(self):
        return self.__dict__

    @classmethod
    def check_permitted(cls, data):
        model_fields = {}
        for key, value in data.items():
            if key in cls.usable_permitted_fields:
                model_fields[key] = value
        # if not len(data) == len(model_fields):
        #     return False
        return model_fields


class ModelList(list):

    def to_json(self):
        """Transforms a model object in json

        Returns:
            str: JSON string representing the object
        """
        return current_app.response_class(
            json.dumps(self, default=json_utils.default_to_json, sort_keys=True, indent=4),
            mimetype=current_app.config['JSONIFY_MIMETYPE']
        )

    def sort_buy(self):
        self.sort(key=lambda x: (x.price, x.creation))
        return

    def sort_sell(self):
        self.sort(key=lambda x: (x.price*(-1), x.creation))
        return

    def insert(self):
        pass

    # def to_json(self):
        # tmp = []
        # for i in self:
        #     tmp.append(i.to_dict())
        # return jsonify(tmp)


class OfferQueue(list):
    pass
