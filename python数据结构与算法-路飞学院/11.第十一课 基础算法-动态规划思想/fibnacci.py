# 递归写法
# 为什么这么慢呢？子问题的重复计算。时间复杂度为2^n
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

print(fibnacci(10))


# 非递归写法 时间复杂度为n。它把算好的结果保存到f中了
def fibnacci_no_rec(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


print(fibnacci_no_rec(10))