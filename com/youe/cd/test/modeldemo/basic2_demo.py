#输出语句：
print("100+200=%d" %(100+200))

#输入语句：
#inputName = input("Please input your name:")
#print("The name you are inputted is:%s" %inputName)

#数据类型：列表list、元组tuple、字典dictionary、set
#list列表
friends = ['xiaoming','ergou','sanmao']
print(friends)
print(friends[0])
print(friends[-1])    #负几表示从后往前数的第几个, -1开始

#添加与删除
friends.append('dapeng')
print(friends)
friends.insert(0, 'diyi')
print(friends)

friends.pop(-1)
print(friends)
friends.pop(2)
print(friends)

#替换
friends[0] = 'diyich'
print(friends)