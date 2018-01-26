import exchange.stock.model as stock_model
import exchange.utils.model_utils as model_utils
import exchange.user.model as user_model
import datetime
from random import randint


class Offer(model_utils.Model):
    permitted_fields = ['id', 'stock', 'user', 'type', 'price', 'quantity', 'creation']
    usable_permitted_fields = []

    def __init__(self, ide, stock, user, typ, price, quantity):
        self.id = ide
        self.stock = stock
        self.user = user
        self.type = typ
        self.price = price
        self.quantity = quantity
        self.creation = datetime.datetime.now()
        self.executed = False

    def change_status(self):
        self.executed = True


DATA = model_utils.ModelList()
STOCK = stock_model.DATA
USER = user_model.DATA
tipo = ['B','S']

for i in range(0, 5):
    j = randint(0, 4)
    k = randint(0, 2)
    h = randint(0,1)
    o = randint(1,1000)
    p = randint(1, 10)
    DATA.append(Offer(i, STOCK[j], USER[k], tipo[h], o, p))
