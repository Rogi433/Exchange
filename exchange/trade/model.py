import exchange.utils.model_utils as model_utils

DATA = model_utils.ModelList()


class Trade(model_utils.Model):
    permitted_fields = ['id', 'b_offer_id', 's_offer_id', 'u_buy_id', 'u_sell_id']
    usable_permitted_fields = []

    def __init__(self, id, b_offer_id, s_offer_id, u_buy_id, u_sell_id):
        self.id = id
        self.b_offer_id = b_offer_id
        self.s_offer_id = s_offer_id
        self.u_buy_id = u_buy_id
        self.u_sell_id = u_sell_id
