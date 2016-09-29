from task.task import update_app_config, app

update_app_config('amqp://guest:guest@192.168.1.200:5673//', 'redis://192.168.1.200:6380/0')

print app.tasks['peoplus.rpc_task'].apply_async(['res.users', 'search_read', [[('id', '<', '2')]]])
