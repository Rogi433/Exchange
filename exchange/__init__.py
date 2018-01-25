from flask import Flask, jsonify, render_template, request, abort, make_response
from werkzeug.exceptions import default_exceptions, HTTPException
import json

app = Flask(__name__)
__all__ = ['make_json_app']


@app.errorhandler(404)
def not_found(error=None):
    return make_response(jsonify({'error': 404, 'message': 'Not Found ' + request.url}), 404)


@app.route('/', methods=['GET'])
def root():
    import exchange.user.controller
    import exchange.stock.controller
    import exchange.offer.controller

    users = exchange.user.controller.get()
    stocks = exchange.stock.controller.get()
    offers = exchange.offer.controller.get()

    ind = {'users': users, 'stocks': stocks, 'offers': offers}

    return jsonify(ind)


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    import exchange.user.controller

    if request.method == 'GET':
        if 'id' in request.args:
            user = exchange.user.controller.get_one(request.args['id'])
            if user:
                return user
            else:
                return not_found(404)
        elif 'name' in request.args:
            user = exchange.user.controller.get_one(request.args['name'])
            if user:
                return user
            else:
                return not_found(404)
        else:
            return exchange.user.controller.get(), 200

    elif request.method == 'POST':
        import exchange.user.model
        if not request.json and not exchange.user.model.User.check_permitted(request.json, exchange.user.model.User.permitted_fields):
            abort(400)
        name = request.json['name']

        return exchange.user.controller.post(name)

    elif request.method == 'DELETE':
        import exchange.user.model
        if not request.json and not exchange.user.model.User.check_permitted(request.json, exchange.user.model.User.permitted_fields):
            abort(400)
        ide = request.json['id']

        return exchange.user.controller.delete(ide)


@app.route('/stocks', methods=['GET'])
def get_stocks():
    import exchange.stock.controller

    if 'id' in request.args:
        stock = exchange.stock.controller.get_one(request.args['id'])
        if stock:
            return stock
        else:
            return not_found(404)
    elif 'label' in request.args:
        stock = exchange.stock.controller.get_one(request.args['label'])
        if stock:
            return stock
        else:
            return not_found(404)
    else:
        return exchange.stock.controller.get()


####################################################################################################
@app.route('/offers', methods=['GET', 'POST'])
def get_or_post_offers():
    if request.method == 'GET':
        import exchange.offer.controller

        if 'id' in request.args:
            return exchange.offer.controller.get_one(request.args['id'])

        return exchange.offer.controller.get()

    elif request.method == 'POST':
        if not request.json or not request.json['stock'] or not request.json['type'] or not request.json['price'] or not request.json['quantity']:
            abort(400)

        import exchange.offer.controller

        offer = request.json
        return exchange.offer.controller.post(offer)



@app.route('/offers/<int:id>', methods=['DELETE'])
def delete_offers(id):
    return 200
####################################################################################################


# @app.route('/index')
# def ind():
#    return render_template('index.html')
#
# @app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
# def api_echo():
#    if request.method == 'GET':
#        return "ECHO: GET\n"
#
#    elif request.method == 'POST':
#        return "ECHO: POST\n"
#
#    elif request.method == 'PATCH':
#        return "ECHO: PACTH\n"
#
#    elif request.method == 'PUT':
#        return "ECHO: PUT\n"
#
#    elif request.method == 'DELETE':
#        return "ECHO: DELETE"

def make_json_app(import_name, **kwargs):
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app


def run():
    app.run(debug=True)
