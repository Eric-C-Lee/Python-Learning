import random

print("请出拳：0 代表石头，1 代表剪刀，2 代表布")

wins = 0 # 赢赢赢
for i in range(5):
    print(f"\n第 {i+1} 局开始：")
    player = int(input("你出拳："))
    computer = random.randint(0, 2)

    if player == computer:
        print("平局！")
    elif (player == 0 and computer == 1) or \
         (player == 1 and computer == 2) or \
         (player == 2 and computer == 0):
        print("你赢了！")
        wins += 1
    else:
        print("你输了！")

    print(f"电脑出拳：{computer}")
    print(f"当前胜利次数：{wins}")

    if wins == 3:
        print("你已经胜利了三局，恭喜你赢麻了")
        break

if wins < 3:
    print("本场游戏结束，你输麻了")