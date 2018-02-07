import exchange.utils.model_utils as model_utils

DATA = model_utils.ModelList()


class Trade(model_utils.Model):
    permitted_fields = ['id', 'b_offer_id', 's_offer_id', 'u_buy_id', 'u_sell_id']
    usable_permitted_fields = []

    def __init__(self, id, b_offer, s_offer, u_buy, u_sell, price, quantity):
        self.id = id
        self.b_offer = b_offer
        self.s_offer = s_offer
        self.u_buy = u_buy
        self.u_sell = u_sell
        self.price = price
        self.quantity = quantity
