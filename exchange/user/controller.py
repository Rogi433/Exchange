from flask import Flask, jsonify
#import exchange
import json

DATA = [{"id": 1, "name": "Ernesto"}, {"id": 2, "name": "Arnaldo"}]
#DATA = {'erro'}


def get():
    if jsonify(DATA):
        return jsonify(DATA), 200
    else:
        return 404


def get_one(var):
    if isinstance(var, int):
        if var < len(DATA):
            return jsonify(DATA[var-1])
        else:
            return False
    elif isinstance(var, str):
        i = 0; j = len(DATA)+1
        while i < len(DATA):
            if var == DATA[i]["name"]:
                j = i
                i = len(DATA)
            else:
                i += 1
        if j < len(DATA):
            return jsonify(DATA[j])
        else:
            return False
    else:
        return False


def post(name):
    i = len(DATA)+1

    DATA.append({"id": i, "name": name})

    return jsonify([{"id": i, "name": name}]), 201

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
