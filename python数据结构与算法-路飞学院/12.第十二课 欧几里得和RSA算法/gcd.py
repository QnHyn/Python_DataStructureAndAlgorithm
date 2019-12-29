# 递归写法
# 这是一个伪递归，和循环效率一样
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_no_rec(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(12, 16))
print(gcd_no_rec(12, 16))