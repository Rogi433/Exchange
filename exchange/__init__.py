from flask import Flask, jsonify, request, abort, render_template
from werkzeug.exceptions import HTTPException
import exchange.user.model as user_model
import exchange.user.controller as user_controller
import exchange.stock.controller as stock_controller
import exchange.offer.controller as offer_controller
import exchange.trade.controller as trade_controller
import exchange.utils.model_utils as model_utils

app = Flask(__name__, static_folder='../static', static_url_path='')


@app.route('/', methods=['GET'])
def root():

    users = user_controller.get()
    stocks = stock_controller.get()
    offers = offer_controller.get()
    ind = model_utils.ModelList()

    ind.append({'offers': offers, 'users': users, 'stocks': stocks})

    return ind.to_json(), 200


@app.route('/users', methods=['GET', 'POST'])
def get_or_post_users():

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
        if not request.json and not permitted:
            abort(400)
        name = permitted['name']
        user = user_controller.post(name)

        if user:
            return user.to_json(), 201
        else:
            return jsonify({'message': 'user already exist'}), 200


@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    user = user_controller.delete(int(id))

    if user:
        return user.to_json(), 200
    else:
        abort(400)


@app.route('/stocks', methods=['GET'])
def get_stock():

    if request.args:
        stock = stock_controller.get_one(request.args)
    else:
        stock = stock_controller.get()
    if stock:
        return stock.to_json(), 200
    else:
        return abort(404)


@app.route('/offers', methods=['GET', 'POST'])
def get_or_post_offers():
    if request.method == 'GET':
        import exchange.offer.controller

        if request.args:
            offer = exchange.offer.controller.get_one(request.args)
            if offer:
                return offer.to_json(), 200
            else:
                return abort(404)

        return exchange.offer.controller.get().to_json(), 200

    elif request.method == 'POST':
        # permitted = user_model.User.check_permitted(request.json)
        # if not request.json or not permitted:
        #     abort(400)
        # todo: implement a check_permitted process to this endpoint

        # offer = request.json
        return offer_controller.post(request.json).to_json()


@app.route('/offers/<int:id>', methods=['DELETE'])
def delete_offers(id):
    # todo: finish this endpoint
    return 200


@app.route('/trades', methods=['GET'])
def get_trades():
    # if not request.args['type']:
    #     abort(400)
    if request.args:
        trade = trade_controller.get_one(request.args)
        if trade:
            return trade.to_json(), 200
        else:
            abort(404)
    else:
        return trade_controller.get().to_json(), 200


@app.route('/index')
def ind():
    return render_template('index.html',)


@app.route('/test')
def test():
    import tests.market as test
    from exchange.offer.model import Offer

    test.test_offers()
    print(' lista de Buy:')
    for x in Offer.BUY:
        print(x.price)
        print(x.quantity)
    print('')
    print(' lista de Sell:')
    for x in Offer.SELL:
        print(x.price)
        print(x.quantity)
    print('')

    users = user_controller.get()
    stocks = stock_controller.get()
    offers = offer_controller.get()
    ind = model_utils.ModelList()

    ind.append({'offers': offers, 'users': users, 'stocks': stocks})

    return ind.to_json(), 200


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

# todo: create a "manual" for the end-points to facilitate tests
