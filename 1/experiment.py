name = 'T$M'
age = 114514
weight = 1919810
print('我的名字不是%s,%d岁，是体重%fmg的学生' % (name, age, weight))
print(f'我不是{name}，{age}岁\n')

# 获取输入信息
name = input('请输入姓名:')
student_id = input("请输入学号：")
address = input("请输入家乡：")
hobby = input("请输入爱好：")
email = input("请输入邮箱：")

# 输出个人信息方格
print("+---------------CV---------------+", "\n               {:<27}".format(name),
      "\n| 学号：{:<27}|".format(student_id),
      "\n| 学号：{:<27}|".format(student_id), "\n| 家乡：{:<27}|".format(address),
      "\n| 爱好：{:<27}|".format(hobby), "\n| 邮箱：{:<27}|".format(email), "\n+--------------脱敏数据--------------+")
