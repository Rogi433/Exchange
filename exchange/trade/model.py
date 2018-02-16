import exchange.utils.model_utils as model_utils
import uuid
import hashlib

DATA = model_utils.ModelList()


class Trade(model_utils.Model):
    permitted_fields = ['id', 'b_offer_id', 's_offer_id', 'u_buy_id', 'u_sell_id']
    usable_permitted_fields = []

    def __init__(self, b_offer, s_offer, price, quantity):
        has = hashlib.sha256()
        has.update(b"str(uuid.uuid4())")
        self.id = has.hexdigest()

        self.b_offer = b_offer
        self.s_offer = s_offer
        self.price = price
        self.quantity = quantity
