import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GamePortal.settings')

app = Celery('GamePortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'action_every_monday_10am': {
        'task': 'GamePortal.tasks.send_weekly_news',
        'schedule': crontab(hour=10, minute=0, day_of_week='monday'),
        'args': (),
    },
}
