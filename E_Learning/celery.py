from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_Learning.settings')

app = Celery('E_Learning')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day': {
        'task': 'accounts.tasks.send_test_message',
        'schedule': crontab(hour=20, minute=22),
    }
}


# app = Celery('E_Learning')
#
# app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request :{self.requst!r}')
