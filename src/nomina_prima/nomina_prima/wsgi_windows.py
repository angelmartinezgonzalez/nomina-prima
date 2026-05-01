import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Python310/Lib/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Apache24NominaPrima/htdocs/src/nomina_prima/')
sys.path.append('C:/Apache24NominaPrima/htdocs/src/nomina_prima/nomina_prima/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'nomina_prima.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nomina_prima.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

