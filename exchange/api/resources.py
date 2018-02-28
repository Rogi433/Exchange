from flask import request, abort
import time
import functools
import webargs
from exchange.utils.model_utils import Model as Model
from flask_restful_swagger_2 import swagger, Resource
from webargs.flaskparser import use_args
from exchange.api import dicts

FIELD_CONSTRUCTOR = dict(integer=webargs.fields.Int,
                         double=webargs.fields.Float,
                         number=webargs.fields.Number,
                         string=webargs.fields.String,
                         boolean=webargs.fields.Boolean)


def create_args(swagger_dict):
    parameters = swagger_dict["parameters"]
    return_dict = dict()
    for parameter in parameters:
        if parameter["in"] == "query":
            constructor = FIELD_CONSTRUCTOR[parameter["type"]]
            args = dict(validate=[])
            keys = parameter.keys()
            if "required" in keys and parameter["required"]:
                args["required"] = True
            if "minimum" in keys:
                minimum = parameter["minimum"]
                args["validate"].append(lambda x: x >= minimum)
            if "maximum" in keys:
                maximum = parameter["maximum"]
                args["validate"].append(lambda x: x <= maximum)
            if "enum" in keys:
                enum = parameter["enum"]
                args["validate"].append(lambda x: x in enum)
            if "default" in keys and "default" in parameter:
                args["default"] = parameter["default"]
                args["missing"] = parameter["default"]
            return_dict[parameter["name"]] = constructor(**args)

    return return_dict


class ApiResponse(Model):

    def __init__(self, caller, *args, **kwargs):

        start = time.time()
        self.result = caller(*args, **kwargs)
        self.runtime = "{0:.4f} seconds".format(time.time() - start)
        self.endpoint = request.path

    @classmethod
    def decorate(cls, caller):

        @functools.wraps(caller)
        def wrapper(*args, **kwargs):
            # encapsulate all response on the ApiResponse
            return cls(caller, *args, **kwargs)

        return wrapper


class Allocation(Resource):
    get = dicts.GET_STOCK
    verify_args_get = create_args(get)

    @ApiResponse.decorate
    @swagger.doc(get)
    @use_args(verify_args_get)
    def get(self, args, allocation_id):
        import exchange.offer.controller

        if request.args:
            offer = exchange.offer.controller.get_one(request.args)
            if offer:
                return offer.to_json(), 200
            else:
                return abort(404)

        return exchange.offer.controller.get().to_json(), 200
