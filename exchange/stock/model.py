import exchange.utils.model_utils as model_utils


class Stock(model_utils.Model):
    permitted_fields = ['id', 'label']
    usable_permitted_fields = []

    def __init__(self, ide, label):
        self.id = ide
        self.label = label


DATA = model_utils.ModelList()

for j, i in enumerate(['FB','AMZN','AAPL','NTFLX','GOOG']):
    DATA.append(Stock(j+1, i))
