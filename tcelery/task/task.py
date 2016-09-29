# coding=utf-8
from celery import Celery
from confmanage.confmanage import tornado_conf
from odoo.handler import Handler

app = Celery()
config = {
    "CELERY_TASK_SERIALIZER": 'json',
    "CELERY_RESULT_SERIALIZER": 'json',
    "CELERY_ACCEPT_CONTENT": ['json'],
    "CELERYD_FORCE_EXECV": True,
    "CELERYD_MAX_TASKS_PER_CHILD": 1024,
    "CELERY_CREATE_MISSING_QUEUES": True,
    "CELERY_TIMEZONE": 'Asia/Shanghai',
    "CELERY_ENABLE_UTC": True,
    "CELERYD_CONCURRENCY": 1,
    "CELERY_DEFAULT_QUEUE": 'peoplus',
    "CELERY_DEFAULT_EXCHANGE": 'peoplus',
    "CELERY_DEFAULT_EXCHANGE_TYPE": 'direct',
    "CELERY_DEFAULT_ROUTING_KEY": 'peoplus',
}


def get_openerp():
    tornado_conf.load()
    conf_dict = tornado_conf.options
    openerp = Handler(conf_dict.get('openerp_path'), conf_dict.get('work_path'), conf_dict.get('conf_path'),
                      conf_dict.get('db_name'))
    return openerp


@app.task(name='peoplus.rpc_task')
def rpc_task(model, method, args=[], kwargs={}):
    '''
    :param model  模型名 如"res.users"
    :param method 方法 如"read"
    :param args 参数
    :param kwargs 参数
    '''
    print '1'
    openerp = get_openerp()
    return openerp.obj_apply(model, method, args, kwargs)


def update_app_config(BROKER_URL, CELERY_RESULT_BACKEND):
    '''
    更新worker配置
    :param BROKER_URL 中间人参数
    :param 任务结果存放地址
    :param 处理哪些数据库的请求
    '''
    config.update(
        {
            "BROKER_URL": BROKER_URL,
            "CELERY_RESULT_BACKEND": CELERY_RESULT_BACKEND,
        }
    )
    app.conf.update(**config)


if __name__ == '__main__':
    import sys
    update_app_config('amqp://guest:guest@192.168.1.200:5673//', 'redis://192.168.1.200:6380/0')
    app.worker_main(argv=sys.argv[0:1])
