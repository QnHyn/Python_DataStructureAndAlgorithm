# 简单版选择排序
def select_sort(li):
    li_new = []
    for i in range(len(li)):
        # 有重复的也没关系，会从左边找
        # min是0(n) remove是一个O(n)
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

import random
list = random.sample([i for i in range(1000)], 20)
print(list)
li_new = select_sort(list)
print(li_new)

# 改进版选择排序
def select_sort_impro(li):
    for i in range(len(li)-1):
        # 假设最小值是无序区的第一个位置
        min_loc = i
        # 可以偷次懒 i 不需要和自己比拉
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

import random

list1= [random.randint(0,1000) for i in range(20)]
print(list1)
select_sort_impro(list1)
print(list1)




