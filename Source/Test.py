from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá mundo"

if __name__ == '__main__':
    app.run(debug=True)

#json.dump()

