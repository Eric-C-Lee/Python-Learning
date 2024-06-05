age = 20
if age >= 18:
    print('已经成年，可以上网')
# 进阶：
age = int(input('请输入您的年龄：'))
if age >= 18:
    print(f'您输入的年龄是{age}, 已经成年，可以上网')
# if…else…条件语句：
age = int(input('请输入您的年龄：'))
if age >= 18:
    print(f'您输入的年龄是{age}, 已经成年，可以上网')
else:
    print(f'您输入的年龄是{age},小朋友，回家写作业去')
# if…elif…多重判断：
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您输入的年龄是{age}, 童工')
elif 18 <= age <= 60:
    print(f'您输入的年龄是{age}, 合法')
elif age > 60:
    print(f'您输入的年龄是{age}, 退休年龄\n')
# if 嵌套：
money = 0
seat = 1
if money == 1:
    print('土豪，请上车')
    if seat == 1:
        print('有空座，坐下了')
    else:
        print('没有空座，站着等....')
else:
    print('朋友，没带钱，跟着跑，跑快点')
# 综合作业 2：根据如下要求，编写一个简单的猜拳小游
