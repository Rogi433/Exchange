from flask import Flask, jsonify, render_template, request, abort, make_response
from werkzeug.exceptions import HTTPException
import exchange.user.model as user_model
import exchange.user.controller as user_controller
import exchange.stock.controller as stock_controller
import exchange.offer.controller as offer_controller
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():

    users = user_controller.get()
    stocks = stock_controller.get()
    offers = offer_controller.get()

    ind = {'users': users.to_json(), 'stocks': stocks.to_json(), 'offers': offers.to_json()}

    return jsonify(ind)


@app.route('/users', methods=['GET', 'POST'])
def get_users():

    if request.method == 'GET':
        if request.args:
            user = user_controller.get_one(request.args)
        else:
            user = user_controller.get()
        if user:
            return user.to_json(), 200
        else:
            return abort(404)

    elif request.method == 'POST':
        permitted = user_model.User.check_permitted(request.json)
        if not request.json and not permitted['name']:
            abort(400)
        name = permitted['name']
        user = user_controller.post(name)

        if user:
            return user.to_json(), 201
        else:
            return jsonify({'message': 'user already exist'}), 200


@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    return user_controller.delete(int(id)).to_json(), 200


@app.route('/stocks', methods=['GET'])
def get_stock():
    import exchange.stock.controller

    if request.args:
        stock = stock_controller.get_one(request.args)
    else:
        stock = stock_controller.get()
    if stock:
        return stock.to_json(), 200
    else:
        return abort(404)


####################################################################################################
@app.route('/offers', methods=['GET', 'POST'])
def get_or_post_offers():
    if request.method == 'GET':
        import exchange.offer.controller

        if 'id' in request.args:
            return exchange.offer.controller.get_one(request.args['id'])

        return exchange.offer.controller.get().to_json(), 200

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


def run():
    @app.errorhandler(Exception)
    def handle_error(error):
        response = jsonify(dict(error=str(error)))
        response.status_code = 500
        if hasattr(error, "code"):
            response.status_code = error.code
        return response

    # for any http status code force json response
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, handle_error)

    app.run(debug=True)
