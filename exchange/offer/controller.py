import exchange.offer.model as offer_model
import exchange.utils.model_utils as model_utils

DATA = offer_model.DATA


def get():
    """
        Gets all offers and return them.
        Could think of implementing pagination later
    """
    return DATA


def get_one(args):
    if args['type']:
        lista = model_utils.ModelList()
        for item in DATA:
            if args['type'] == item.type:
                lista.append(item)
        return lista
    
    for item in DATA:
        for key, value in args.items():
            if str(getattr(item, key)) == value:
                return item
    return False


def post(args):

    return 201


def delete(offer_id):
    
    return 200

#incomplete