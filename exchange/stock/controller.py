import exchange.stock.model
import exchange.utils.model_utils
DATA = exchange.stock.model.DATA


def get():
    return DATA


def get_one(args):
    for item in DATA:
        for key, value in args.items():
            if str(getattr(item, key)) == value:
                return item
    return False
