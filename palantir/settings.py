MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'palantir'

RESOURCE_METHODS = ['GET', 'POST']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

PAGINATION_LIMIT = 1000

pools_schema = {
    'ip': {
        'type': 'string',
        'minlength': 7,
        'maxlength': 15,
        'required': True,
        'unique': True,
    },
    'coin': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 60,
        'required': True,
    },
    'location': {
        'type': 'dict',
        'string': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
        },
        'latitude': {
            'type': 'number',
            'minlength': -90,
            'maxlength': 90,
        },
        'longitude': {
            'type': 'number',
            'minlength': -180,
            'maxlength': 180,
        }
    },
}
pools = {
    'item_title': 'pool',
    'additional_lookup': {
        'url': 'regex("(?:\d{1,3}\.){3}\d{1,3}")',
        'field': 'ip',
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': pools_schema,
}

DOMAIN = {
    'pools': pools,
}
