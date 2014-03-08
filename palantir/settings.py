MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'palantir'

RESOURCE_METHODS = ['GET', 'POST']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']



pools_schema = {
    'ip': {
        'type': 'string',
        'minlength': 7,
        'maxlength': 15,
    },
}
pools = {
    'item_title': 'pool',

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': pools_schema,
}

DOMAIN = {
    'pools': pools,
}
