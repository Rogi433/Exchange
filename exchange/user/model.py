import exchange.utils.model_utils
import uuid


class User(exchange.utils.model_utils.Model):
    permitted_fields = ['id', 'name', 'deleted']
    usable_permitted_fields = ['name']

    def __init__(self, nome):
        self.id = str(uuid.uuid4())
        self.name = nome
        self.deleted = False

    def delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False


DATA = exchange.utils.model_utils.ModelList()

for item in ['Ernesto', 'Arnaldo', 'Fred']:
    DATA.append(User(item))

# Precisa achar um jeito de implementar o json_utils
# Precisa ajeitar o controller do user e o __init__ para o método DELETE
