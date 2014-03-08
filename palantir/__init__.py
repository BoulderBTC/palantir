import os
from eve import Eve
filepath = os.path.dirname(os.path.realpath(__file__)) + '/settings.py'

app = Eve(settings=filepath)
