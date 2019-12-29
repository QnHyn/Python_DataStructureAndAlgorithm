import time
import functools


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__)
        print("%s running time is:%s sesc." % (func.__name__, t2 - t1))
        return result
    return wrapper

