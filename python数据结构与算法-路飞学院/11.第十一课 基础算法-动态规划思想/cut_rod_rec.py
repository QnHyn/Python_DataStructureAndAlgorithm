import time


def cal_time(func):
    def wrapper(*args,  **kwargs):
        t1 = time.time()
        result = func(*args,  **kwargs)
        t2 = time.time()
        print(func.__name__)
        print("%s running time is:%s sesc." % (func.__name__,  t2 - t1))
        return result
    return wrapper


# 钢条切割问题的递归写法一
def cut_rod_recursion1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recursion1(p, i) + cut_rod_recursion1(p, n-i))
        return res


# 钢条切割问题的优化后的递归写法
def cut_rod_recursion2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cut_rod_recursion2(p, n-i))
        return res


# 加装饰器计算时间
@cal_time
def c1(p, n):
    return cut_rod_recursion1(p, n)


@cal_time
def c2(p, n):
    return cut_rod_recursion2(p, n)


# 显然c2更快一些 指数爆炸
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
#p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# c1 running time is:2.3339221477508545 sesc.
# c2 running time is:0.01692795753479004 sesc.
print(c1(p, 15))
print(c2(p, 15))