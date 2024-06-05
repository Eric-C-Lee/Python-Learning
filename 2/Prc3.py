import random

n = int(input("请输入飞镖次数："))
count = 0
i = 0

while i < n:
    # 落点坐标 (x,y)
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1:
        count += 1
    i += 1

pi = 4 * count / n
print("圆周率的近似值为：", pi)