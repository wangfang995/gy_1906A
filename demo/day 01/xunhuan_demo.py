# 九九乘法表
for b in range (1,10):
    for c in range(1, b + 1):
        print(c, "x", b, "=", c * b, '\t', end='')
    print()

# 九九乘法表
for i in range (9):
    for u in range (i+1):
        print((u +1 ),"x",(i + 1),'=',(i + 1) * (u +1 ),'\t',end='')
    print()

#九九乘法表
for i in range (9):
    for a in range (9):
        if (a <= i):
            print(i+1,'x', a+1,'=',(i+1)*(a+1),"\t",end='')
    print()

count = 0
for i in range(100):
    if(i%2==1):
        count = count+1
        print("第",count,"个奇数是",i)

#求100以内的质数
for i in range (2,100):
    n = 2
    for j in range (2,i+1):
        if(i%n == 0):
            break
        n = n+1
    if(n == i):
        print(i)

