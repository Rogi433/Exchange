from exchange.offer.model import Offer
import exchange.utils.model_utils as model_utils
import exchange.stock.controller as stock_controller
import exchange.user.controller as user_controller
import exchange.trade.allocation as trade


DATA = model_utils.ModelList()
DATA.append({'Bid': Offer.BUY})
DATA.append({'Ask': Offer.SELL})


def get():
    """
        Gets all offers and return them.
        Could think of implementing pagination later
    """
    return DATA


def get_one(args):
    if args['side'] == 'B':
        if args['type']:
            lista = model_utils.ModelList()
            for item in Offer.BUY:
                if args['type'] == item.type:
                    lista.append(item)
            return lista
    
        for item in Offer.BUY:
            for key, value in args.items():
                if str(getattr(item, key)) == value:
                    return item
    else:
        if args['type']:
            lista = model_utils.ModelList()
            for item in Offer.SELL:
                if args['type'] == item.type:
                    lista.append(item)
            return lista

        for item in Offer.SELL:
            for key, value in args.items():
                if str(getattr(item, key)) == value:
                    return item

    for i in range(0, 1):
        if i == 0:
            side = 'Bid'
        else:
            side = 'Ask'

        for item in DATA[i][side]:
            for key, value in args.items():
                if str(getattr(item, key)) == value:
                    return item
    return False


def post(json):
    print(' price ', json['price'], ' side ', json['side'], ' stock ', json['stock'], ' quantity ', json['quantity'])

    # todo: test if market orders are working

    if json['type'] == 'market':
        stock = stock_controller.get_one(json['stock'])

        user = user_controller.get_one(json['user'])

        if user and stock and json['side']:
            offer = Offer(stock, user, json['side'], float('inf'), json['quantity'])
            trade.trade(offer)
            return offer
        else:
            return False
    else:
        stock = stock_controller.get_one(json['stock'])
        user = user_controller.get_one(json['user'])
        if user and stock and json['side']:
            offer = Offer(stock, user, json['side'], json['price'], json['quantity'])
            trade.trade(offer)
            return offer
        else:
            return False


def delete(offer_id):
    
    return True


#incomplete