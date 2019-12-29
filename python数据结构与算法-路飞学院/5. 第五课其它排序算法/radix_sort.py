# 基数排序算法
def radix_sort(li):
    # 循环次数即位数由最大值确定。
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        # 桶数确定的10个
        buckets = [[] for _ in range(10)]
        # 根据位数。个位十位百位..放入桶中
        for val in li:
            # 987 it=1 987//10->98 98%10->8; it=2 987//100->9 9%10=9
            digit = (val // (10 ** it)) % 10
            buckets[digit].append(val)
        # 分桶完成
        li.clear()
        for buc in buckets:
            # 重新写回li
            li.extend(buc)

        it += 1


import random
list = [random.randint(0, 1000) for i in range(20)]
print(list)
radix_sort(list)
print(li)
