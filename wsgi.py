import os
import django
from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('/home/pi/WeddingSite') 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeddingSite.settings')

application = get_wsgi_application()

