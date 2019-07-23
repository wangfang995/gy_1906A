#有参数，有返回值
def a (q1,w2,m3 ):
    return "{q2}欠{w3}{m4}钱".format(q2=q1,w3=w2,m4=m3)
print(a ("q1","w2","m3" ))

#默认值
def buy_coffees(cups,cash = 100):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
buy_coffees(3)



