from datetime import timedelta

BROKER_URL = 'mongodb://localhost:27017/palantir'

CELERY_TIMEZONE = 'UTC'

CELERYBEAT_SCHEDULE = {
    'everytensec': {
      'task': 'palantir.tasks.get_pools',
      'schedule': timedelta(seconds=600),
    },
}
