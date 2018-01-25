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

    i = len(DATA)+1
    n_user = exchange.user.model.User(i, name)
    DATA.append(n_user)

    return n_user


def delete(id):
    print('oi')
    DATA[id-1] = DATA.delete_user(DATA[id-1])
    return DATA[id]

# Entender porque quando eu faço um POST, depois se eu fizer GET de novo ele atualiza DATA
#
# Como decidir os status http?
# Tentar implementar o codigo de "response" para controlar o status:
#    from flask import json
#
#    @app.route('/summary')
#    def summary():
#        data = make_summary()
#        response = app.response_class(
#            response=json.dumps(data),
#            status=200,
#            mimetype='application/json'
#        )
#        return response
#
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

#for item in data:
#   for key, value in args.item():
#       if hasattr(item, key) and item.get(key) == value:
#           return item
#       return False
