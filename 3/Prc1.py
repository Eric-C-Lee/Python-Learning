import random

num = random.randint(1, 10)  # 生成随机数
count = 0  # 猜测次数

while count < 10:
    guess = int(input("请猜一个1~10之间的整数："))
    count += 1
    if guess == num:
        if count == 1:
            print("太棒啦，一次就中了")
        elif count <= 3:
            print("还不错呀，猜%d次就中了" % count)
        elif count <= 5:
            print("一般般哟，猜%d次就中了" % count)
        else:
            print("太笨啦，猜%d次才猜对" % count)
        break
    else:
        print("猜错了，还有%d次机会" % (10 - count))

if count == 10:
    print("太笨啦，10次都没猜对")
