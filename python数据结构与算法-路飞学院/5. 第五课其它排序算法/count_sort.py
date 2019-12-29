# 计数排序 已知需要排序的列表元素范围在0-100之间
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


import random
list = [random.randint(0,100) for i in range(1000)]
print(list)
count_sort(list)
print(list)
