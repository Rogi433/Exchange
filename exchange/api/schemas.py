from flask_restful_swagger_2 import Schema


class StockSchema(Schema):
    type = 'object'

    properties = {
        "example": {
            'type': 'integer'
        }
    }

    example = {
        "example": 2
    }