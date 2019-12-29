import heapq # 它可以用来实现优先队列
import random


list = random.sample([i for i in range(100)], 10)
print(list)
heapq.heapify(list) # 构建堆的过程(默认小根堆)
for i in range(len(list)):
    # 每次弹出最小的数
    print(heapq.heappop(list), end=",")