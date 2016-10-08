# coding=utf-8
from celery.schedules import crontab
from datetime import timedelta
from celery import Celery

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'exec_5_seconds': {
        'task': 'peoplus.task',
        'schedule': timedelta(seconds=5),
        'args': (),
    },
}
app = Celery('periodic.app')
if __name__ == '__main__':
    app.conf.update(
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERYD_FORCE_EXECV=True,
        CELERYD_MAX_TASKS_PER_CHILD=1024,
        CELERY_CREATE_MISSING_QUEUES=True,
        CELERY_TIMEZONE='Asia/Shanghai',
        CELERY_ENABLE_UTC=True,
        CELERYD_CONCURRENCY=1,
        CELERY_DEFAULT_QUEUE='peoplus',
        CELERY_DEFAULT_EXCHANGE='peoplus',
        CELERY_DEFAULT_EXCHANGE_TYPE='direct',
        CELERY_DEFAULT_ROUTING_KEY='peoplus',
        CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE
    )
    app.worker_main()
