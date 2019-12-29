# 假设穿过来的列表两段有序
def merge(li, low, mid, high):
    '''
    :param li:  归并的列表
    :param low: 第一个有序列表的起始点
    :param mid: 第一个有序列表的终止点
    :param high: 第二个有序列表的终止点
    :return:
    '''
    # 指针移动, 变量记录指针
    i = low
    j = mid + 1
    ltmp = []
    # 左右两边都有数时
    while i <= mid and j <= high:
        # 因为移动的指针,不能原地排序.开辟列表储存值
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # 只有一边有数了
    # 只有左边有数
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    # 只有右边有数
    while j <= high:
        ltmp.append(li[j])
        j += 1
    # 把ltmp 写回到li
    li[low: high+1] = ltmp


# 测试merge函数
# li = [2, 4, 5, 7, 1, 3, 6, 8]
# merge(li, 0, 3, 7)
# print(li)


def merge_sort(li, low, high):
    # 递归直到low和high相等。只有一个元素
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        # print(li[low:high+1])
        merge(li, low, mid, high)


if __name__ == "__main__":
    import random
    list = random.sample([i for i in range(100)], 10)
    print(list)
    merge_sort(list, 0, len(list)-1)
    print(list)