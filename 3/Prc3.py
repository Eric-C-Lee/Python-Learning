for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end='\t')
    print()

# 第二部分
a=9
while a>=1:
    b=1
    while b<=a:
        print(f"{b}*{a}={a*b}",end='\t')
        b+=1
    print()
    a-=1
