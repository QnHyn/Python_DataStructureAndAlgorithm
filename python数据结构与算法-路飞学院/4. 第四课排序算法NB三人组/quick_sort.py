# 快速排序算法
# 首先，实现partition归位函数
from cal_time import cal_time

def partition(li, left, right):
    '''
    :param li:  接收的列表
    :param left: 列表对应的左边指针
    :param right: 列表对应的右边指针
    :return:返回中间位置的指针给quick_sort
    '''
    # 将第一位置存起来，第一个位置是left。因为之后还有传来列表的切片。
    tmp = li[left]
    while left < right:
        # 右边开始找，找比tmp小的值。
        # 假如li[right] = tmp是因为一直找不到while左右直接碰上，还会自己减一。
        # right就会跑到left左边，这是我们不希望的所以left < right限制一下。
        # 不能去掉li[right] = tmp,列表中可能有其他重复的数字。
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        # 同理，从左边开始找，找比tmp大的值
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]

    # 这里左右指针汇合left和right指向同一个位置
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    # 至少有两个元素, 一个元素排什么序呀
    # 这里可千万别傻傻的.(后面都不要出现固定的位置0或len(li)-1,迭代会傻眼的)
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)



if __name__ == "__main__":
    import random
    list = random.sample([i for i in range(100)], 10)
    print(list)
    quick_sort(list, 0, len(list) - 1)
    print(list)

