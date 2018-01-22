from flask import Flask, jsonify, render_template, request, abort, Response
import json

app = Flask(__name__)


@app.errorhandler(404)
def not_found(code=None, msg=None):
    if msg is None:
        msg = 'Not Found: ' + request.url
    message = {
        'status': code,
        'message': msg,
    }
    resp = jsonify(message)
    resp.status_code = code

    return resp


@app.route('/', methods=['GET'])
def root():
    import exchange.user.controller
    import exchange.stock.controller
    import exchange.offer.controller

    users = exchange.user.controller.get()
    stocks = exchange.stock.controller.get()
    offers = exchange.offer.controller.get()

    ind = [users, stocks, offers]

    return jsonify(ind)


@app.route('/users', methods=['GET'])
def get_users():
    import exchange.user.controller

    if 'id' in request.args:
        print('etapa 1')
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
        return exchange.user.controller.get()


@app.route('/users/<string:name>', methods=['POST'])
def post_users(name):
    import exchange.user.controller

    return exchange.user.controller.post(name)


@app.route('/stocks', methods=['GET'])
def get_stocks():
    import exchange.stock.controller

    return jsonify(exchange.stock.controller.get()), 200


@app.route('/offers', methods=['GET'])
def get_offers():
    import exchange.offer.controller

    return jsonify(exchange.offer.controller.get()), 200


# Como fazer uma route que recebe mais de um parametro para criar uma nova offer (metodo POST)


@app.route('/hello', methods=['GET'])
def api_hello():
    data = {
        'hello': 'world',
        'number': 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

    # @app.route('/index')
    # def ind():
    #    return render_template('index.html')

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
    app.run(debug=True)
