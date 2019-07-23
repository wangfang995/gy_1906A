def sum (num1,num2 ):
    sum = num1 + num2
    print(num1 ,"+" , num2 , "=" ,sum)
    return sum #返回值
def cha (num1,num2):
    cha = num1 - num2
    print(num1, "-", num2, "=",cha)

def ji (num1,num2):
    ji = num1 * num2
    print(num1, "*", num2, "=", ji)
    return ji
def shang (num1,num2):
    if (num2!=0):
        shang = num1 / num2
        print(num1, "/", num2, "=", shang)
    else:
        print("除数不能为0")


ji(ji (2,2),2)

# with open("D:\\softwareData\\Python\\biancheng\\demo\\day 04\\suanshu.txt")as a:
#     b = a.readlines( )
#     for i in b:
#         i = i.replace("\n"," ")
#         i = i.split(",")
#         sum(int(i[0]), int(i[1]))
#         cha(int(i[0]), int(i[1]))
#         ji(int(i[0]), int(i[1]))
#         shang(int(i[0]), int(i[1]))