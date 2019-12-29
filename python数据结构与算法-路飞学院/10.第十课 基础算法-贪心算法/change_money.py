# n是需要找给人的钱
t = [100, 50, 20, 5, 1]


def change(t, n):
    m = [0 for i in range(len(t))]
    for ind, money in enumerate(t):
        m[ind] = n // money
        # n是暂时没找开的钱
        n = n % money
    return m, n

print(change(t, 376))