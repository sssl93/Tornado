from time import time
from celery import group
from celery_test import hello, add, add_full, add_callback,retry_task
from celery.task.http import HttpDispatch
from celery.task.http import URL

# res = URL('http://localhost:48090/http_task_test').get_async()
# res = HttpDispatch.delay(url='http://localhost:48090/http_task_test', method='post', x=10, y=10)
# print res.get()
# result=add.apply_async(queue='videos',link=[add_callback.s(),hello.s()],compression='zlib')
# result = add_callback.apply_async((1,),queue='videos',link=add.s)
# res = group(add.subtask()for i in range(10)).apply_async()
# print res.get()
# print result.id
result=retry_task.apply_async(queue='videos',)

