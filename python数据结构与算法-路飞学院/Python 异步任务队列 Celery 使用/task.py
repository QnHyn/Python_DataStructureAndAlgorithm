import time
from celery import Celery

# 实例化一个Celery
broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'


# 参数1 自动生成任务名的前缀
# 参数2 broker 是我们的redis的消息中间件
# 参数3 backend 用来存储我们的任务结果的
app = Celery('my_task', broker=broker, backend=backend)


# 加入装饰器变成异步的函数
@app.task
def add(x, y):
    print('Enter call function ...')
    time.sleep(4)
    return x + y


if __name__ == '__main__':
    # 这里生产的任务不可用，导入的模块不能包含task任务。会报错
    print("Start Task ...")
    result = add.delay(2, 8)
    print("result:", result)
    print("End Task ...")

# Start Task ...
# result: c88a6fab-6923-4324-96e7-c1c8a36719d9
# End Task ...
# 这里并没有启动worker, 它只是把任务发给redis中
# -A tasks 是app实例的位置task.py
# -l info 是输出日志的级别为info
# win10有坑需要安装pip install eventlet不然报错ValueError: not enough values to unpack (expected 3, got 0)
# win10有坑启动worker:celery -A task worker -l info -P eventlet
# celery -A <mymodule> worker -l info -P eventlet