from flask import current_app
import exchange.utils.json_utils as json_utils
import json
import exchange.utils.model_utils as model_utils
import datetime
import uuid


class Offer(model_utils.Model):

    BUY = model_utils.ModelList()
    SELL = model_utils.ModelList()

    permitted_fields = ['id', 'stock', 'user', 'side', 'price', 'quantity', 'creation']
    usable_permitted_fields = ['stock', 'price', 'type', 'quantity', 'user', 'side']

    def __init__(self, stock, user, side, price, quantity):
        self.id = str(uuid.uuid4())
        self.stock = stock
        self.user = user
        self.side = side
        self.price = price
        self.quantity = quantity
        self.creation = datetime.datetime.now()
        self.executed = 0

    def update_quantity(self, qtd):
        if self.quantity >= qtd:
            self.quantity -= qtd
            self.executed += qtd
        else:
            self.executed += self.quantity
            self.quantity = 0

    # def change_status(self):
    #     self.executed = True

        # todo: create a order book separating the different stocks.
        # One way of doing it is, maybe, create a class OfferList that inherits ModelList and
        # has its own to_json() that separates the stocks when the request is made
