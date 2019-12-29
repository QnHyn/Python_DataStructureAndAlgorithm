# 桶排序
def bucket_sort(li, n=100, max_num=10000):
    # 创建桶列表, 桶也是一个列表。所以应该是一个二维列表
    buckets = [[] for _ in range(n)]
    for val in li:
        # 0-99 ->0, 100-199->1
        # 10000->100 我们这只有0-99号桶。所以把10000放到99号桶
        i = min(val // (max_num // n), n-1) # 放到i号桶中
        buckets[i].append(val)
        # 插入后先桶内排序
        for j in range(len(buckets[i])-1, 0, -1):
            # 桶内冒泡排序
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    # 输出所有桶内元素
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

import random
list = [random.randint(0, 10000) for i in range(100)]
print(list)
li = bucket_sort(list)
print(li)

