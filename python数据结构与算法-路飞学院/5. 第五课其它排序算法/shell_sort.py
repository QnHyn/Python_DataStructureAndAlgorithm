# 希尔排序,只需要把插入排序拿过来。把出现的1 变为gap即可
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)): # i表示摸到的牌
        temp = li[i]
        j = i - gap # j表示有序区的最后一张牌(手里的牌)
        while j >= 0 and li[j] > temp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = temp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

import random
list = random.sample([i for i in range(1000)], 20)
print(list)
shell_sort(list)
print(list)