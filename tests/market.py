"""
    This file is used to simulate a market to test the trade algorithm
"""
import exchange.stock.model as stock_model
import exchange.offer.model as offer_model
import exchange.offer.controller as offer_controller
import exchange.user.model as user_model
from random import randint, uniform


STOCK = stock_model.DATA
USER = user_model.DATA
side = ['B', 'S']


def test_offers():
    for _ in range(0, 5):
        json = {
            'stock': {
                'label': STOCK[randint(0, 4)].label
            },
            'user': {
                'name': USER[randint(0, 2)].name
            },
            'side': side[randint(0, 1)],
            'price': uniform(1, 1000),
            'quantity': randint(1, 20),
            'type': 'limit',
        }

        # todo: try to make this work sending the user id
        offer_controller.post(json)
