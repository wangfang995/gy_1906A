a ='http://qa.yansl.com/#/pms/addProduct'
xieyi=a.split("://")[0]
a= a.split("://")[1]
yuming = a[:a.find("/")]
uri = a[a.find("/"):]
print(xieyi,yuming,uri)

b ={}
b['协议']=xieyi
b['ip']=yuming
b['uri']=uri
print(b)
