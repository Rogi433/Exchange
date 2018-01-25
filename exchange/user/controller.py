from flask import Flask, jsonify
import exchange.user.model
import exchange.utils.model_utils
import json
#DATA = [{"id": 1, "name": "Ernesto"}, {"id": 2, "name": "Arnaldo"}]

DATA = exchange.utils.model_utils.ModelList()
u1 = exchange.user.model.User(1, 'Ernesto')
u2 = exchange.user.model.User(2, 'Arnaldo')
u3 = exchange.user.model.User(3, 'Fred')

DATA.append(u1.to_json())
DATA.append(u2.to_json())


def get():
    return DATA.to_json()


def get_one(var):
    if isinstance(var, str):
        i = 0; j = len(DATA)+1
        while i < len(DATA):
            if var == DATA[i]['name']:
                j = i
                i = len(DATA)
            else:
                i += 1
        if j < len(DATA):
            return jsonify(DATA[j])
        else:
            if int(var) <= len(DATA):
                return jsonify(DATA[int(var) - 1])
            else:
                return False
    else:
        return False


# Implement later the delete protocol. When you create a new user you have to check the list for
#other users that where deleted and the you update their information. Otherwise you just create
#a new user the old way


def post(name):
    i = len(DATA)+1

    n_user = exchange.user.model.User(i, name)
    DATA.append(n_user.to_json())

    return jsonify([{"id": i, "name": n_user.name}]), 201


def delete(id):
    user = DATA[id]
    user.delete()
    return 200

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
