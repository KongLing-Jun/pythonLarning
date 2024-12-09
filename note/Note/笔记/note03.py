# print("hello pycharm")  # 注释
# 这段代码不会执行
'''
注释
'''
# """
# 注释
# """
# 变量：记录事物变化的过程
# 变量: "先定义，在引用"
# name = 'Alan'
# print(type(name))
# age = 18
# print(type(age))
"""
垃圾回收机制
"""
# 引用计数增加
# a = 100
# b = a
# c = a
# 引用计数减少
# del a
# print(a)
# del b
# print(b)
# c = 123
# print(c)
# python内置功能 一但发现引用计数为0的,立刻把内存空间回收
# 变量三大组成部分
# 1.变量名

# avg = (67.5 + 89.0 + 12.9 + 32.2) / 4  # 平均值
# total = (67.5 - avg) ** 2 + (89.0 - avg) ** 2 + (12.9 - avg) ** 2 + (32.2 - avg) ** 2  # x**2表示x的2次方
# result = total / 4 - 1  # 方差
# a = 2 ** 3  # x**3表示x的3次方
# print(a)
# print(avg)
# print(result)
'''
print(1 + 2 - 3)
print(1 + 1 / 3)
'''
'''
变量名命名要见名知意
age = 18
price =84
变量名组成必须是字母数字下划线
_res=9
name = 'Alan'
一般大写表示常量，小写表示变量
Price = 54
price = Price
print(price)
age_of_cat = 3
'''
# 2. 赋值符号 =
# 3. 变量值
'''
x = '中'
name = 121
a = 3.1415926
b = 4
d = 34583
# id 变量名的内存地址
'''
'''
print(bin(id(name)))  # 二进制
print(oct(id(name)))  # 八进制
print(hex(id(name)))  # 十六进制
print(chr(name))  # 将一个整数转化为字符
print(ord(x))  #将一个字符转化为整数
print(int(a))  #将a转换为整型
print(float(b)) #将b转换为浮点型
print(complex(3, 4))  #输出复数(3+4j)
print(str(d))  #将d转化为字符串类型
'''
# type 变量名的类型
'''
name = 'Alan'
age  = 10
print(type(name))
print(type(age))
level = 1
level =level + 1
print(level)
print(10+2)
print(10-2)
print(10*2)
print(10/2)
'''
# a = 'Alan'
# b = 'Alan'
# print(a, b)
# print(id(a), id(b))

# PIE = 3.1415926
# AGE = 18
'''
a = 3
b = 1.5
c = a + b
print(c, type(c))

age = 20
print(age > 12)
print(age>35)
'''
'''
name = 'Alan'
age = 73
price = 3.5

# 元祖
z = (45, 67, 'Alan', (67, 78, 'Dio', (89, 34, 'Mark')))
print(z[3][3][2])

# 列表
# 从前往后数  0 1 2 3
# 从后往后前  -4 -3 -2 -1
# 列表一般是用来存同一类属性，同一样事物不同的状态用列表的嵌套。
# 列表是索引对应值
l = [45, 67, 'Alan', ['aaa', 'bbb']]
print(l[-2])

hobbies = ['可乐', '厕所', '烫头']
print(hobbies[1])

person = [
    ['Mark', 22, 100, ['纯友谊']],
    ['Dio', 21, 50, ['我服了']],
    ['Alan', 21, 30, ['画饼']]
]
print(type(person))
for i in range(3):
    for j in range(4):
        if j != 3:
            continue
        print(person[i][j], end=' ')
    print()

# print(person[0][0], person[0][3])
# print(person[1][3])
# print(person[2][3])
'''
'''
# 字典类型dict
# 字典是key对应值  通常为字符串类型
# 列表与字典可以相互嵌套
person = [{'name': 'Mark', 'age': 22, 'height': 169, 'sex': 'man', 'say': ['纯友谊', 'one']},
          {'name': 'Dio', 'age': 21, 'height': 175, 'sex': 'man', 'say': ['我服了', 'two']},
          {'name': 'Alan', 'age': 20, 'height': 170, 'sex': 'man', 'say': ['画饼', 'three']},
          {'name': 'PoloV', 'age': 20, 'height': 170, 'sex': 'man', 'say': ['纯友谊', 'four']},
          {'name': 'Carla', 'age': 20, 'height': 145, 'sex': 'woman', 'say': ['How have your been', 'five']},
          {'name': 'Fancy', 'age': 20, 'height': 175, 'sex': 'man', 'say': ['泰裤辣', 'six']}
          ]
print(person[4]['height'])
print(person[4]['say'][0])
print(person)
'''
'''
# 布尔类型
a = True
b = False
print(type(a))
print(type(b))

a = 1
b = 0
c = None
print(type(c))
# 0 None ''[] {} 代表False

name = 'Mark' # 直接访问
l = ['Dio','Alan',name] #间接访问
print(l)
print(id(name))
print(id(l[2]))
'''
'''
a=100
b=a
c=a
print(id(a))
print(id(b))
print(id(c))
'''
# 列表不会存放真正的值，只存放索引和值的内存地址，值会存放单独的内存空间
# 引用计数，标记清除，分代回收
'''
name = 'Alan'
l = ['a','b',name]
name = 'Mark'
print(l[2])
print(name)
'''
'''
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']
l1.append('d')  # 把d尾添加到l1
l1.append(l2)
# print(l1)
# print(id(l2),id(l1[4]))
l2.append(l1)
# #print(l2)
# print(id(l1),id(l2[3]))
del l1  # 解除l1这个变量名与它这个列表的绑定关系
del l2  # 解除l2这个变量名与它这个列表的绑定关系
# 就是前面列表的引用计数少了一个
# 这叫循环引用，会导致非常致命问题-内存泄漏
'''
# 程序与用户交互
# name = input('请输入你的名字：')
# print(name,type(name))
'''
age = input('请输入你的年龄：')
print(age,type(age))
age = int(age)
print(age,type(age))
print((age+1))
temp = int('123')
print(temp,type(temp))
'''
# 一.格式化字符串
'''
# 1.%
# info = ('my name is %s, I am from %s.' % ('Alan', 'Foshan'))
# print(info)
# info1 = 'my name is %s' % 'Alan'
# print(info1)
# %s接受任意的类型 %d 接受整型类型
info = ('my name is %(name)s, I am from %(hometown)s.' % {'name': 'Alan', 'hometown': 'Foshan'})
print(info)
info1 = 'my name is %s' % 18
print(info1)
info2 = 'my name is %s' % ['a', 'b']
print(info2)
info3 = 'my name is %s' % {'a': 'aa', 'b': 'bb'}
print(info3)

# 2.format()
info = 'my name is {0} , I am from {1} '.format('Alan', 'Foshan')
print(info)
info1 = 'my name is {name} , I am from {hometown} '.format(name='Alan', hometown='Foshan')
print(info1)
'''
'''
# 二.格式化填充
# ****开始****
a = '{0:*^10}'.format('开始')  # ^居中
b = '{0:*<10}'.format('开始')
c = '{0:*>10}'.format('开始')
d = '{hometown:*^10}'.format(name='Alan', hometown='Foshan')
f = '{num:.2f}'.format(num=3.1415926)  # .2f保留2位小数    .xf保留x位小数
print(a)
print(b)
print(c)
print(d)
print(f)
'''
'''
# 三.f
name = input('请输入你的名字：')
hometown = input('请输入你的家乡：')
info = f'我的名字是{name},我来自于{hometown}'
print(info)
# 四.string-Template(需要导入）
'''
'''
# 算数运算符 +-*/% //
print(10 + 5.5)
print(10 - 5.5)
print(10 * 5.5)
print(10 / 5.5)
print(10 % 5.5)  # 取模，去余数
print(10 // 5.5)  # 地板除
print(2 ** 3)  # 2的3次方
# 比较运算符 > < == >= <= !=
print(20 > 18)
print(20 < 18)
print(20 == 18)
print(20 >= 18)
print(20 <= 18)
print(20 != 18)
name =input('请输入你的名字：')
print(name=='Alan')
'''
'''
# 整型 ，浮点型，字符串类型，列表类型，字典类型，布尔类型
# 可变类型：值改变的情况下，id不变，说明改的是原值   列表类型，字典类型
# 不可变类型：值改变的情况下，id变了，说明改的不是原值 整型，浮点型，字符串类型，布尔类型
name = 'PoloV'
print(id(name))
name = 'Alan'
print((id(name)))

l =['James','PoloV','Alan']
print(id(l))
l[1] = 'Mark'
print(l)
print(id(l))
'''
'''
# 显式布尔值
# 明天=='周三'->True
# 年龄<18->False
# True False

# 隐式布尔值
# 0 None 空(空字符串，空列表，空字典)->False
# 其他所有的值都是True
#'Alan'->True
#''->False
#'   '->True
#[],{}->False

if 条件：
    代码
'''
