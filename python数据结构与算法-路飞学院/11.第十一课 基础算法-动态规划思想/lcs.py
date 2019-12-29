def lcs_length(x, y):
    m = len(x)
    n = len(y)
    # m+1行 n+1列 因为图中要从0开始(空串是所有序列的子序列)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # 从1到m和n
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                # 图中斜着传递值情况 最后一个字母匹配来自左上方
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    # 调试逐行打印
    for _ in c:
        print(_)
    return c[m][n]

def lcs(x, y):
    m = len(x)
    n = len(y)
    # m+1行 n+1列 因为图中要从0开始(空串是所有序列的子序列)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # b储存箭头方向 1左上方, 2上方, 3左边 0 没有方向
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 从1到m和n
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # 图中斜着传递值情况 最后一个字母匹配来自左上方
                c[i][j] = c[i - 1][j - 1] + 1
                # 储存左上的箭头
                b[i][j] = 1
            elif c[i][j - 1] < c[i - 1][j]:
                # 从上方来
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    return c[m][n], b


def lac_traceback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1: # 来自于左上方匹配可输出
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2: # 来自于上方
            i -= 1
        else:# 来自于左方
            j -= 1
    return "".join(reversed(res))


#print(lcs_length("ABCBDAB", "BDCABA"))
print(lac_traceback("ABCBDAB", "BDCABA"))


