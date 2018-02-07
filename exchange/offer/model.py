from flask import current_app
import exchange.utils.json_utils as json_utils
import json
import exchange.utils.model_utils as model_utils
import datetime


class Offer(model_utils.Model):
    _id = 0

    BUY = model_utils.ModelList()
    SELL = model_utils.ModelList()

    permitted_fields = ['id', 'stock', 'user', 'side', 'price', 'quantity', 'creation']
    usable_permitted_fields = ['stock', 'price', 'type', 'quantity', 'user', 'side']

    def __init__(self, stock, user, side, price, quantity):
        self._id += 1
        self.id = self._id
        self.stock = stock
        self.user = user
        self.side = side
        self.price = price
        self.quantity = quantity
        self.creation = datetime.datetime.now()
        self.executed = False

    def change_status(self):
        self.executed = True

        # todo: create a order book separating the different stocks.
        # One way of doing it is, maybe, create a class OfferList that inherits ModelList and
        # has its own to_json() that separates the stocks when the request is made
