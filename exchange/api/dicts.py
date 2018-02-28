from exchange.api import schemas as schemas

GET_STOCK = {
    'tags': ['Stock'],
    'description': 'Gets a stock',
    'parameters': {
        'name': 'label',
        'description': 'Stock Label',
        'in': 'query',
        'type': 'string',
        'required': True
    },
    'responses': {
        '200': {
            'description': 'OK',
        },
        '400': {
            'description': 'Validation error'
        },
        '404': {
            'description': 'Account not found'
        }
    }

}