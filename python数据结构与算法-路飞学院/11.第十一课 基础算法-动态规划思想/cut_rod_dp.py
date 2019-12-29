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


# 钢条切割问题的动态规划写法
@cal_time
def cut_rod_dp1(p, n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j] + r[i-j])
        r.append(res)
    return r[n]


def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0  #价格的最优质值
        res_s = 0  #价格最大值方案的左边不切割长度
        for j in range(1, i + 1):
           if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


# 根据s输出我们的解决方案
def cut_rod_solution(p, n):
    tmp = n
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return "%s段切割方案为:%s,切割后最大价格为%s" % (tmp, ans, r)


# 显然c2更快一些 指数爆炸
#p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
#print(cut_rod_dp1(p, 9))
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(cut_rod_solution(p, 9))