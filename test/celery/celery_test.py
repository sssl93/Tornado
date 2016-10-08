from celery import Celery
from kombu import Exchange, Queue
from datetime import timedelta
from celery.schedules import crontab
import time
from celery import task
import celery

app = Celery('hello')
app.conf.update({
    'BROKER_URL': 'amqp://guest:guest@192.168.1.183//',
    'CELERY_RESULT_BACKEND': 'amqp://guest:guest@192.168.1.183//',
    'CELERY_ROUTES': {
        'celery_test.hello': {'queue': 'videos', 'routing_key': 'media.video'},
        'celery_test.add': {'queue': 'videos', 'routing_key': 'media.video'},
        'celery_test.add_callback': {'queue': 'videos', 'routing_key': 'media.video'},
    },
    'CELERY_QUEUES': (
        # Queue('default', Exchange('default'), routing_key='default'),
        Queue('videos', Exchange('media'), routing_key='media.video', auto_declare=False),
        # Queue('images', Exchange('media'), routing_key='media.image',auto_declare=False),
    ),
    'CELERYBEAT_SCHEDULE': {
        'add-every-monday-morning': {
            'task': 'celery_test.add',
            'schedule': timedelta(seconds=10),
            'args': ()
            # "options":{'queue':'default'}
        },
        'CELERY_IMPORTS': 'celery.task.http',
    }
})


@app.task()
def hello(uuid):
    time.sleep(1)
    print 'hello world', uuid
    return 'hello world'


@app.task
def add():
    # print 'This is %s' % (x,)
    # print 'This is %s' % (y,)
    time.sleep(1)
    print "--------------------", time.time()


@app.task
def add_full(x, y):
    print 'x is:%s   ' % (x,)
    print 'y is:%s   ' % (y,)
    return x + y


@app.task
def add_callback(uuid):
    time.sleep(2)
    print '--------------------------------call_back_success-------------------: %s' % (uuid,)
    return uuid


@app.task(bind=True, default_retry_delay=10, max_retries=5)
def retry_task(self):
    print '----------http----------------'
    try:
        f = open('txt.txt', 'r')
    except Exception as e:
        print 'Exception-----', e
        self.retry(exe=e)


if __name__ == '__main__':
    b = app.Beat()
    b.run()
