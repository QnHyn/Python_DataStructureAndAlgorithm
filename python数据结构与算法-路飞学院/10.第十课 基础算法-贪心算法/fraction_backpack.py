goods = [(60, 10),(100, 20),(120, 30)] # 每个商品元组表示(价格，重量)
goods.sort(key=lambda x:x[0]/x[1], reverse=True)
#print(goods)


def fraction_backpack(goods, w):
    m = [0 for i in range(len(goods))]
    total_prize = 0
    for ind, (money, weight) in enumerate(goods):
        if w >= weight:
            m[ind] = 1
            total_prize += money
            w -= weight
        else:
            m[ind] = w / weight
            w = 0
            total_prize += money * m[ind]
            break
    return m, total_prize


print(fraction_backpack(goods, 50))


