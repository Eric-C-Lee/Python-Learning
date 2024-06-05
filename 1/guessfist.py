# 定义手势
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# 定义手势列表 石头 布 剪刀
gestures = [rock, paper, scissors]

# 定义胜利条件 限制三局，至少一次
winning_combinations = [(0, 2), (1, 0), (2, 1)]


# 定义游戏规则
def play_game():
    player_score = 0  # 初始化分数
    computer_score = 0
    while player_score < 2 and computer_score < 2:  # 循环
        # 让玩家选择手势
        print("请选择手势：", "\n0: 石头", "\n1: 布", "\n2: 剪刀")
        player_choice = int(input())  # 记录玩家
        print("你出了：")
        print(gestures[player_choice])  # 显示手势

        # 电脑生成
        computer_choice = random.randint(0, 2)
        print("电脑出了：")
        print(gestures[computer_choice])  # 显示手势

        # 判断胜负
        if (player_choice, computer_choice) in winning_combinations:  # 胜利条件：限制三局，至少一次
            print("你赢了这一局！\n")
            player_score += 1
        elif (computer_choice, player_choice) in winning_combinations:
            print("电脑赢了这一局！\n")
            computer_score += 1
        else:
            print("这一局平局！\n")

        # 打印当前比分
        print("当前比分：", "\n你：", player_score, "\n电脑：", computer_score)

    # 判断最终胜负
    if player_score > computer_score:
        print("你赢了游戏！")
    else:
        print("电脑赢了游戏！")


# 运行游戏
play_game()
