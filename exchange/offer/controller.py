import exchange.offer.model as offer_model

DATA = offer_model.DATA

def get():
    """
        Gets all offers and return them.
        Could think of implementing pagination later
    """
    return DATA


def get_one(id_str):
    id = int(id_str)
# Gets one offer receiving its id (as string) as a parameter. Returns the offer as json and status 200 if it finds it
#and returns status 404 if it doesnt
    return 200


def post(dict):

    return 201

#incomplete