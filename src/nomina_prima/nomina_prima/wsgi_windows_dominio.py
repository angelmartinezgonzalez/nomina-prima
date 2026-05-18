"""
WSGI config for nomina_prima project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import site
import sys

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Python314/Lib/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Apache24NominaPrima/demo1/src/nomina_prima/')
sys.path.append('C:/Apache24NominaPrima/demo1/src/nomina_prima/nomina_prima/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'nomina_prima.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nomina_prima.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

