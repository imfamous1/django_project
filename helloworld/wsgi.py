import os
import sys

path = '/home/zkokorin/django_project'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'helloworld.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()