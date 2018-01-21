from flask import Flask, jsonify, render_template

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

    return jsonify(ind)


@app.route('/users')
def get():
    import exchange.user.controller

    if jsonify(exchange.user.controller.get()):
        return jsonify(exchange.user.controller.get()), 200
    else:
        return 404


@app.route('/users/<string:name>')
def post(name):
    import exchange.user.controller

    return jsonify(exchange.user.controller.post(name)), 200


    #@app.route('/index')
    #def ind():
    #    return render_template('index.html')


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