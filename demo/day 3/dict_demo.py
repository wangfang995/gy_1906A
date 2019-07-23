#字典的特性：
#1.字典中的key是唯一的
#2.key是不可改变的
# 元组（1,2，3）可以当key,但是元组（1,2，[3]）是不可以当key的
# 可以用字符串，数字，元组（不可包含list-列表）
#3.字典中排序是无序的
#4.只能通过key访问valuce

#创建字典
a = {}

#字典中新增一对数据
a["喜欢吃什么"]= "烤鸭"
print(a)

a[1] = 123
print(a)

#字典中的修改
a["喜欢吃什么"]= "红烧肉"
print(a)

# #删
# # 删除某一对值
# a.pop(1)
# print(a)
# #清空字典
# a.clear()
# print(a)

#查
#根据key查value
print(a["喜欢吃什么"])
#遍历字典
for i in a:
    print(a["喜欢吃什么"])

#合并
#把一个字典合并到另一个字典
c = {"姓名":"小明","性别":"男"}
d = {"喜欢吃什么":"烤鸭"}
# c.update(d)
# print(c)
#两个字典合并，形成一个新的字典,两表不发生改变
print(dict(c,**d))

#成员判断，只支持key
if ("性别" in c):
    print('存在字典中')
else:
    print('不存在字典中')

#获取字典中的长度
print(len(c))