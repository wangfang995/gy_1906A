#小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
a = 20
if(a >= 5):
    print("小明可以买大前门")
if(a >= 10):
    print("小明可以买红双喜")
if(a>= 25):
    print("小明可以买玉溪")

#成人票 200 12岁以下的小孩票100 60岁以上的老人票 150 小明今年18岁，去买票应该买那种票？
b = 18
if (b < 18 ):
    print(b,"小明可以买未成年票")
elif (b >= 60):
    print(b,"小明可以买老人票")
else:
    print("只能买成人票")



