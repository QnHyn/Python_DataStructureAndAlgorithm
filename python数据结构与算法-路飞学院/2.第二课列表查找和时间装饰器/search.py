from cal_time import cal_time


# 线性查找
@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return None


# 二分查找
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 在左边
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


if __name__ == "__main__":
    import random
    list = [i for i in range(1000)]
    print(list)
    res = binary_search(list, 999)
    print(res)

    list = random.sample([i for i in range(1000)], 999)
    print(list)
    res = linear_search(list, 4)
    print(res)
