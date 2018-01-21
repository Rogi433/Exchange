#import exchange

DATA = [{"id": 1, "name": "Ernesto"}, {"id": 2, "name": "Arnaldo"}]
#DATA = {'loucura'}

def get():

    #response = exchange.app.response_class(response=json.dumps(DATA), status=200, mimetype='users/json')

    return DATA


def post(name):
    i = len(DATA)+1

    DATA.append({"id": i, "name": name})

    return [{"id": i, "name": name}]

# Entender porque quando eu faço um POST, depois se eu fizer GET de novo ele atualiza DATA