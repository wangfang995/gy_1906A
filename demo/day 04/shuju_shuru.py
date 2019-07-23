
#按照扑克牌的规则，现在有6张牌，只要5张
#黑桃（S）红桃（H）方块（D）梅花（C）
#牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
#数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
#[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
#["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
#["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]


#从控制台输入
def juge_3_2 (a):
    # a = input("请输入牌型：" )
    # 第一步：统一符号  对字符串的处理，用replace（）
    a = (a.replace("''", '"'))
    #print(a)
    # 第二步：去掉中括号 字符串截取  [::]
    a = a[2:-2]
    #print(a)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b = a.split('" , "')
    #print(b)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    c = {}
    for i in b:
        d = (i[1:])
        #print(d)
        # 第五步：统计相同的数字个数  用字典去统计
        if (d in c):
            c[d] += 1
        else:
            c[d] = 1
    #print(c)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    v1 = 0
    v2 = 0
    for i in c:
        if (c[i] == 3):
            v1 = 1
        if (c[i] == 2):
            v2 = 1
    if (v1 == 1 and v2 == 1):
        print("可以三带二")
    else:
        print("不可以三代二")
# for e in range(3):
    # juge_3_2()


#从文件读取内容
#open python 提供的一个内置函数，作用就是打开一个文件，参数一：文件的路径 参数二：打开文件的模式，r只读，w 可写入（清空之前文件内容） a 可读可写入（在文件内容末端接着写）
#with open() as f 类似于 f = open ()他可以在with 的代码执行出问题的时候,做一些资源释放的工作
with open("D:\\softwareData\\Python\\biancheng\\demo\\day 04\\cards.txt","r") as f:
# 读文件.readlines()作用就是把文件中整个内容按行读取出来,存到一个list中;read()把整个文件的内容读取出来,存到一个字符串中
   lines = f.readlines()
#for循环遍历这个列表
for line in lines:
        #去掉每一行末尾的换行附
        line = line.replace("\n",'')
        print(line)
        #调用一个方法，判断是否可以3带2
        juge_3_2(line)



#int 字符串强转成数字
#str 数字强转成字符串