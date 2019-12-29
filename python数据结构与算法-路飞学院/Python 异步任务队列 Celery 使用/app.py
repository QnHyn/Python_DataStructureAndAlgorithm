import time
#from task import add
from celery_app import task1, task2

if __name__ == '__main__':
    print("Start Task ...")
    result1 = task1.add.delay(2, 8) # 或apply_async也可以
    result2 = task2.multiply.delay(3, 8)
    print("result1:", result1)
    print("result2:", result2)
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
