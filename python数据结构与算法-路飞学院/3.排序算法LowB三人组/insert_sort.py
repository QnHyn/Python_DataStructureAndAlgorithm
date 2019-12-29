# 插入排序
def insert_sort(li):
    for i in range(1, len(li)): # i表示摸到的牌
        temp = li[i]
        j = i - 1 # j表示有序区的最后一张牌(手里的牌)
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


import random
list = random.sample([i for i in range(1000)], 20)
print(list)
insert_sort(list)
print(list)
