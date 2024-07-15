from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_Learning.settings')

app = Celery('E_Learning')

app.config_from_object('django.conf:settings', namespace='CELERY')

app = Celery('E_Learning')
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
