from celery import Celery

@app.task
def hehe(x, y):
    print 'x is:%s   ' % (x,)
    print 'y is:%s   ' % (y,)
    return x + y