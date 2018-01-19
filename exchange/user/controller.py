from flask import json

DATA = [{"name": "Ernest"}, {"name": "Arnoldo"}]

def get():

    return DATA

def post(name):

    DATA.append({"name": name})

    return [{"name":name}]

# Entender porque quando eu faço um POST, depois se eu fizer GET de novo ele atualiza DATA