import exchange.stock.model as stock_model
import exchange.user.model as user_model
from random import randint
import exchange.utils.model_utils as model_utils
import datetime


class Offer(model_utils.Model):
    permitted_fields = ['id', 'stock', 'user', 'type', 'price', 'quantity', 'creation']
    usable_permitted_fields = ['stock', 'price', 'type', 'quantity', 'user']

    def __init__(self, ide, stock, user, side, typ, price, quantity):
        self.id = ide
        self.stock = stock
        self.user = user
        self.side = side
        self.price = price
        self.quantity = quantity
        self.creation = datetime.datetime.now()
        self.executed = False
        self.type = typ

    def change_status(self):
        self.executed = True


BUY = model_utils.ModelList()
SELL = model_utils.ModelList()

STOCK = stock_model.DATA
USER = user_model.DATA
mode = ['B', 'S']

for i in range(0, 5):
    j = randint(0, 4)
    k = randint(0, 2)
    h = randint(0, 1)
    o = randint(1, 1000)
    p = randint(1, 10)
    DATA.append(Offer(i, STOCK[j], USER[k], mode[h], 'limit', o, p))
