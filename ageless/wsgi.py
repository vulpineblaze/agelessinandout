"""
WSGI config for ageless project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ageless.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()



# import os
# import sys

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ageless.settings")

application = get_wsgi_application()