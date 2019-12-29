'''
    这里出数时,没有必要去在开辟内存空间。重新建一个列表,可以用列表切片划分堆和有序位置(用high来表示最后一个最元素的位置)。
    需要i和j分别指当前层和下面一层
    sift函数中可以合并else分支，但是不利于理解所以不合并了。
    父亲i找孩子：左孩子2*i+1, 右孩子2*i +2
	孩子p找父亲：左右孩子(p-1)//2
'''


def sift(li, low, high):
    '''
    :param li: 待调整的堆列表
    :param low: 待调整的堆的堆顶位置(根节点位置)
    :param high:待调整的堆的最后一个元素位置(防止调整越界)
    :return:
    '''
    i = low
    j = 2 * i + 1
    # 保存需要堆顶元素放到它该放到的位置
    tmp = li[low]
    while j <= high:  # j位置有数就一直循环
        if (j + 1) <= high and li[j + 1] > li[j]:  # 右孩子有并且比左边的孩子更大
            j = j + 1  # 把j指向右边孩子
        if li[j] > tmp:
            li[i] = li[j]
            # j位置就空下来了,朝下继续找合适元素(更新i和j,继续往下找)
            i = j
            j = 2 * i + 1
        else:  # tmp 更大
            li[i] = tmp  # 这个父节点可以放tmp。可以做个官(不一定是最大的官)
            break
    else:
        li[i] = tmp  # 把tmp放到孩子节点上


def heap_sort(li):
    n = len(li)
    # 先建堆,农村包围城市方法
    for i in range((n-2)//2, -1, -1):
        # i 构建堆时的调整部分的根位置low
        # high位置精准确定比较麻烦，我们用n-1来代替high的作用(防止调整函数中j越界)
        # 农村堆也位于整个对列表中
        sift(li, i, n-1)
    # 构建堆完成，开始挨个出数
    for k in range(n-1, -1, -1):
        li[0], li[k] = li[k], li[0]
        sift(li, 0, k-1)


if __name__ == "__main__":
    import random
    list = random.sample([i for i in range(100)], 10)
    print(list)
    heap_sort(list)
    print(list)

