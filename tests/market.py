"""
    This file is used to simulate a market to test the trade algorithm
"""
import exchange.stock.model as stock_model
import exchange.offer.model as offer_model
import exchange.offer.controller as offer_controller
import exchange.user.model as user_model
from random import randint

#
# STOCK = stock_model.DATA
# USER = user_model.DATA
# side = ['B', 'S']
#
# for i in range(0, 5):
#     j = randint(0, 4)
#     k = randint(0, 2)
#     h = randint(0, 1)
#     o = randint(1, 1000)
#     p = randint(1, 10)
#     offer_controller.post(offer_model.Offer(i, STOCK[j], USER[k], side[h], 'limit', o, p).to_json())
