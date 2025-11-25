import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ii.settings')

import django
from django.template.loader import get_template

django.setup()

try:
    tmpl = get_template('index.html')
    try:
        origin = tmpl.origin.name
    except Exception:
        origin = repr(tmpl.origin)
    print('TEMPLATE ORIGIN:', origin)
except Exception as e:
    print('ERROR:', e)
