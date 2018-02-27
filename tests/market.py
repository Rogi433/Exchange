"""
    This file is used to simulate a market to test the trade algorithm
"""
import exchange.stock.model as stock_model
import exchange.offer.controller as offer_controller
import exchange.user.model as user_model
from random import randint, uniform


STOCK = stock_model.DATA
USER = user_model.DATA
side = ['B', 'S']


def test_offers():
    for _ in range(0, 10):
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

        offer_controller.post(json)


def test_offers2():
    json = {
        'stock': {
            'label': STOCK[0].label
        },
        'user': {
            'name': USER[0].name
        },
        'side': side[1],
        'price': 100,
        'quantity': 10,
        'type': 'limit',
    }

    offer_controller.post(json)

    json = {
        'stock': {
            'label': STOCK[0].label
        },
        'user': {
            'name': USER[0].name
        },
        'side': side[1],
        'price': 50,
        'quantity': 10,
        'type': 'limit',
    }

    offer_controller.post(json)

    json = {
        'stock': {
            'label': STOCK[0].label
        },
        'user': {
            'name': USER[0].name
        },
        'side': side[0],
        'price': 90,
        'quantity': 10,
        'type': 'limit',
    }

    offer_controller.post(json)
