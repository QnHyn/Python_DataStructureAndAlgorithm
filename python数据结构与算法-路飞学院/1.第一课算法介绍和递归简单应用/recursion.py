def fun1(x):
    if x > 0:
        fun1(x - 1)
        print(x)

def fun2(x):
    if x > 0:
        print(x)
        fun1(x - 1)

fun1(4) # 1 2 3 4
fun2(4) # 4 3 2 1

# 汉诺塔问题
i = 0
def hannoi(n, a, b, c):
    global i
    if n > 0:
        hannoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        i += 1
        hannoi(n-1, b, a, c)


hannoi(3, 'A', 'B', 'C')
print(i)