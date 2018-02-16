from flask import Flask, jsonify
import exchange.user.model
import exchange.utils.model_utils
DATA = exchange.user.model.DATA


def get():
    return DATA


def get_one(args):
    for item in DATA:
        for key, value in args.items():
            if str(getattr(item, key)) == value:
                return item
    return False


def post(name):
    for item in DATA:
        if item.name == name:
            if item.deleted:
                item.restore()
                return item
            return False

    n_user = exchange.user.model.User(name)
    DATA.append(n_user)

    return n_user


def delete(id):
    item = 0
    chose = False
    while item < len(DATA):
        if DATA[item].id == id:
            chose = item
            item = len(DATA)
        item += 1

    if chose:
        DATA[chose].delete()
        return DATA[chose]
    else:
        return False

# get_json(force=False, silent=False, cache=True)
#   Parses the incoming JSON request data and returns it. By default this function will return None if the mimetype is not application/json but this can be overridden by the force parameter. If parsing fails the on_json_loading_failed() method on the request object will be invoked.
#    Parameters:
#
#        force – if set to True the mimetype is ignored.
#        silent – if set to True this method will fail silently and return None.
#        cache – if set to True the parsed JSON data is remembered on the request.
#
# is_json
#    Indicates if this request is JSON or not. By default a request is considered to include JSON data if the mimetype is application/json or application/*+json.
#
#    New in version 0.11.
#
# json
#    If the mimetype is application/json this will contain the parsed JSON data. Otherwise this will be None.
#
#    The get_json() method should be used instead.