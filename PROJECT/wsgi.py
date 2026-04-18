import os
import sys
from django.core.wsgi import get_wsgi_application

# Loyiha ildizini Python yo'liga qo'shish
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')

application = get_wsgi_application()