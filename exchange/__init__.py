from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    import exchange.user.controller
    import exchange.stock.controller
    import exchange.offer.controller

    users = exchange.user.controller.get()
    stocks = exchange.stock.controller.get()
    offers = exchange.offer.controller.get()

    ind = [users, stocks, offers]

    print('index page')

    return jsonify(ind)


@app.route('/users')
def get():
    import exchange.user.controller

    return jsonify(exchange.user.controller.get())


@app.route('/users/<string:name>')
def post(name):
    import exchange.user.controller

    return jsonify(exchange.user.controller.post(name))


def run():
    app.run(debug=True)

    #implementar o codigo de "response" para controlar o status:
    #from flask import json
    #
    #@app.route('/summary')
    #def summary():
    #    data = make_summary()
    #    response = app.response_class(
    #        response=json.dumps(data),
    #        status=200,
    #        mimetype='application/json'
    #    )
    #    return response