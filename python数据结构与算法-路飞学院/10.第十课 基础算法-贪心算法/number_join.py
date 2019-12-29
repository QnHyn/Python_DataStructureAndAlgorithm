from functools import cmp_to_key


li = [32, 94, 128, 1286, 6, 71]
def xy_cmp(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


def number_join(li):
    # 把列表变为字符串列表
    li = list(map(str, li))
    print(li)
    li.sort(key=cmp_to_key(xy_cmp), reverse=False) # 默认就是False
    return "".join(li)

print(number_join(li))