import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ii.settings')

import django
from django.urls import resolve

django.setup()

try:
    match = resolve('/')
    view = match.func
    print('VIEW:', view)
    try:
        print('VIEW MODULE:', view.__module__)
        print('VIEW NAME:', getattr(view, '__name__', repr(view)))
    except Exception:
        pass
except Exception as e:
    print('ERROR:', e)
