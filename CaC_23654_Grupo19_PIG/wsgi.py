"""
WSGI config for CaC_23654_Grupo19_PIG project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CaC_23654_Grupo19_PIG.settings')

application = get_wsgi_application()
