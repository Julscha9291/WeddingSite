import os
import django
from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('/home/pi/WeddingSite') 
sys.path.append('/home/pi/WeddingSite/mysite') 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

