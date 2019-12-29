# 冒泡排序

def bubble_sort(li):
    # 整个列表的循环是n-1趟
    for i in range(len(li)-1):
        # i=0 第一趟 无需区 len(li)-1
        # i=1 第二趟 无需区 len(li)-1-1
        # i=n-1 第n-1趟 无需区 len(li)-1-(n-1)
        # 第i趟 无序区的长度为len(li)-1-i
        for k in range(len(li)-1-i):
            if li[k] > li[k+1]:
                li[k], li[k+1] = li[k+1], li[k]


import random
list = random.sample([i for i in range(1000)], 20)
print(list)
bubble_sort(list)
print(list)


def bubble_sort_impro(li):
    for i in range(len(li) - 1):
        exchange = False
        for k in range(len(li) - 1 - i):
            if li[k] > li[k + 1]:
                li[k], li[k + 1] = li[k + 1], li[k]
                exchange = True
        if not exchange:
            return


import random

list1= [random.randint(0,1000) for i in range(20)]
print(list1)
bubble_sort_impro(list1)
print(list1)