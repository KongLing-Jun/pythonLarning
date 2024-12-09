# 第二章

# 字面量/常量/定量
# int = 666
# float =13.14
# str = 'Alan'
# print(int,float,str)

# 变量：存储计算结果或表示值得抽象概念
# 格式：变量名称 = 变量的值
# 特点：变量可变，可以随时重新赋值
# name = 'belinda'
# name1 ="belinda"
# name2 = '''belinda'''
# print(name)
# print(name1)
# print(name2)
# money = 50
# print("钱包还有:",money)
# money = money - 10
# print("钱包还有:",money)
# 作业：
# money = 50
# spend1 = 10
# spend2 = 5
# print('钱包还有：',money)
# money = money - spend1
# print('钱包还有：',money)
# money = money - spend2
# print('钱包还有：',money)

# 基本数据类型
# string 字符串类型 用引号引起来的数据都是字符串
# int    整型(有符号)  数字类型，存放整数 -1 10 0
# float  浮点数(有符号) 数据类型，存放小数-3.14,6.66
# 通过type()语句的使用方式访问数据类型
# 方法1:使用print直接输出类型信息
# print(type(555))
# print(type(3.45))
# print(type('hadsome'))
# 方法2：使用变量存储type()语句的结果
# name = 'Alan'
# age = 20
# height = 171.3
# print(name,type(name))
# print(age,type(age))
# print(height,type(height))
# 方法3:使用type()语句,查看变量存储的数据类型信息
# name = 'KLJ'    #把'klj'->name
# name_type = type(name) # 'klj'的类型 ->name_type
# print(name_type)  #打印变量名name_type
# 我们通过type(变量)可以输出类型,查看的变量的类型还是数据的类型
# 查看的是变量存储的数据的类型，变量无类型，数据有类型
# age = 20
# age_type = type(age)
# print(age_type)

# 数据类型转换
# 例子:文件：字符串->数字
# int(x) 将x转换为一个整数
# float(x) 将x转换为一个浮点数
# str(x) 将x转换为一个字符串
# 将数字类型转换成字符串
# num_str = str(11)
# print(num_str)
# float_str = str(13.14)
# print(float_str,type(float_str))
# # 将字符串转换成数字类型
# number = int('11')
# print(number,type(number))
# number1 = float('13.14')
# print(number1,type(number1))
# #错误示例:想要字符串转换数字，必须要求字符串的内容都是数字
# num3 = int('Alan')
# print(num3)
# 整数转浮点数
# number = float(1314)
# print(number)
# print(type(number))
# float_num = float(3)
# print(float_num)
# #浮点数转整数
# int_num = int(3.14) #丢失精度
# print(int_num)
# number1 = int(3.1415926)
# print(number1)
# print(type(number1))
# 结论：任何类型都可以转换为字符串,字符串不一定转换为数字类型或其他类型

# 标识符
# 含义: 在python中用来给变量起名字，给方法起名字，给类起名字
# Python中，标识符命名的规则主要有3类：
# • 内容限定
# • 大小写敏感
# • 不可使用关键字

# 标识符命名规则1 —— 内容限定
# 标识符命名中，只允许出现：
# •英文
# •中文
# •数字
# •下划线（_）
# 这四类元素。其余任何内容都不被允许。
# 注意：1. 不推荐使用中文 2.数字不可以开头

# 标识符命名规则2 —— 大小写敏感
# 以定义变量为例：
# Andy = “安迪1”
# andy = “安迪2”
# 字母a的大写和小写，是完全能够区分的。

# 标识符命名规则3 —— 不可使用关键字
# Python中有一系列单词，称之为关键字，关键字在Python中都有特定用途，我们不可以使用它们作为标识符
# import keyword
# print(keyword.kwlist)
# 算数运算符
# print("1 + 1 =",1 + 1)
# print("2 - 1 =",2 - 1)
# print("3 * 3 =",3 * 3 )
# print("4 / 2 =",4 / 2)
# print("11 // 3 =",11 // 3)
# print("9 % 2 =",9 % 2)
# print("2 ** 2 =",2 ** 2)

# 赋值运算符
# num = 1
# num += 1
# num = num + 1
# print("num+= 1:",num)
# num = 2
# num -= 1
# print("num-= 1:",num)
# num = 3
# num *= 1
# print("num*= 1:",num)
# num = 4
# num /= 1
# print("num/= 1:",num)
# num = 5
# num %= 1
# print("num%= 1:",num)
# num = 6
# num **= 2
# print("num**= 2:",num)

# 字符串扩展
# 1.字符串的定义方式：
#1.单引号定义法：可以内含双引号
# name1 = 'Alan'
# print(type(name1))
# # 2.双引号定义法：可以内含单引号
# name2 = "Alan"
# print(type(name2))
# # 3.三引号定义法：
# name3 = '''Alan'''
# print(type(name3))
# 可以使用转义字符(\)来将引号解除效用，变成普通字符串
# name2 = '\'Alan\''
# print(name2)
# name3 = "\"Alan\""
# print(name3)
# #在字符串内，可以内含双引号
# name = '"Alan"'
# print(name)
# #在字符串内，可以内含单引号
# name1 = "'Alan'"
# print(name1)

# 2.字符串拼接
# 字符串字面量直接的拼接
# print("Alan" + "is" + "good")
# 字符串字面量与字符串变量的拼接
# name = 'Alan'
# address = '佛山'
# telephone = 13420684857
# print("我是:" + name + " 我住:" + address + " 电话:" + str(telephone))

# 3.字符串的格式化
# 当变量过多时，我们会发现上述的字符串拼接并不好用，由此引出字符串格式化这个方法。
# 其中的%s
# • % 表示：我要占位
# • s 表示：将变量变成字符串放入占位的地方
# 所以，综合起来的意思就是：我先占个位置，等一会有个变量过来，我把它变成字符串放到占位的位置
# 1.通过占位的形式，完成字符串的拼接
# name = "Alan"
# message = "%s来学习Python" % name
# print(message)

# name1 = "belinda"
# message = "%s来学习Python" % name1
# print(message)

# 2.通过占位的形式，完成数字和字符串的拼接
# python中,支持许多数据类型占位
# %s 将内容转换成字符串，放入占位位置中
# %d 将内容转换成整数，放入占位位置中
# %f 将内容转换成浮点型，放入占位位置中

# class_num  = 29
# avg_grade = 88.56
# message = "数据结构与算法课程，全班%d人，平均分%f" % (class_num,avg_grade)
# print(message)
#
# class_num1 = 30
# avg_grade1 = 78.45
# course = "综合英语"
# message1 ="%s, 全班%d, 平均分%f"% (course,class_num1,avg_grade1)
# print(message1)

# name = 'Alan'
# age = 20
# avg = 84.33
# message = print("姓名:%s,年龄:%d,成绩:%f" % (name,age,avg))
# 3.通过语法：f"内容{变量}"的格式来快速格式化
# name = "Alan"
# birth = "2003-10-19"
# age = 20
# height = 171.3
# print(f"姓名:{name},生日:{birth},年龄:{age},身高:{height}")

# name1 ="belinda"
# birth1 ="2003-11-06"
# age1 = 20
# height1 =150
# print(f"姓名：{name1},生日：{birth1},年龄：{age1},身高：{height1}")

# 4.格式化的精度控制
# 我们可以使用辅助符号"m.n"来控制数据的宽度和精度   3475845.678
# m,控制宽度，要求是数字(很少使用),若设置的宽度小于数字自身，不生效
# .n.控制小数点精度，要求是数字,会进行小数的四舍五入
# • %5d ：表示将整数的宽度控制在 5 位，如数字 11 ，被设置为 5d ，就会变成： [ 空格 ][ 空格 ][ 空格 ]11 ，用三个空格补足宽度。
# • %5.2f ：表示将宽度控制为 5 ，将小数点精度设置为 2
# 小数点和小数部分也算入宽度计算。如，对11.345设置了%7.2f 后，结果是：[空格][空格]11.35。2个空格补足宽度，小数部分限制2位精度后，四舍五入为 .35
# %.2f：表示不限制宽度，只设置小数点精度为2，如11.345设置%.2f后，结果是11.35
# num1 = 11
# num2 = 11.345
# print("数字11宽度限制5,结果是:%5d" % num1)
# print("数字11宽度限制1,结果是:%1d" % num1)
# print("数字11.345宽度限制7,小数精度2,结果是:%7.2f" % num2)
# print("数字11.345宽度不限制,小数精度2,结果是:%.2f" % num2)
# num3 = 3.1415926
# print("结果是：%4.2f"% num3)
# num4 =7777.7777
# print("结果是：%6.3f"% num4)

# 5.对表达式进行格式化
# 表达式:一条具有明确执行结果的代码语句
# 如：
# 1 + 1、5 * 2，就是表达式，因为有具体的结果，结果是一个数字
# 又或者，常见的变量定义：
# name = “张三”     age = 11 + 11
# 等号右侧的都是表达式呢，因为它们有具体的结果，结果赋值给了等号左侧的变量。
# print("1 + 1 的结果是: %d" % (1 * 1))
# print(f"1 * 2 的结果是: {1 * 2}")
# print("字符串在Python中的类型名是: %s" % type("字符串"))
# 如何格式化表达式？
# 1.f"(表达式)"
# 2."%s\%d\%f" % (表达式，表达式，表达式)

# 作业
# name = "小飞象"
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
# stock_price *= stock_price_daily_growth_factor ** growth_days
# print("每日增长系数是:%.1f,经过%d天的增长后，股票达到了:%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price))

# 数据输入input()函数
# • 使用 input() 语句可以从键盘获取输入
# • 使用一个变量接收（存储） input 语句获取的键盘输入数据即可
# • 要注意，无论键盘输入什么类型的数据，获取到的数据永远都是字符串类型
# 获取键盘的输入信息
# name  = input("请告诉我你是谁？")
# print("我知道了，你是%s" % name)
# #输入数字类型
# num= input("请告诉我你的密码:")
# print("你的密码类型是：", type(num))
# # 作业
# user_name = input("请输入你的名字:")
# user_type = input("请输入用户类型:")
# print(f"用户的名字：{user_name},你的用户类型{user_type}")

# 字符串的大小比较
# 在程序中，字符串所用的所有字符如:
# 1.大小写的英文单词 2.数字 3.特殊符号(!,@,#,$,%，<，^，&，*，)都有对应的ASCII码表值。
# 每个字符都能对应上一个：数字的码值，字符串的大小比较就是基于数字的码值大小进行比较的。
# 字符串是按位比较，也就是一位位进行比较，只要有一位大于另一位，那么整体就大.
# 比较 abc abd
# print(f"abd大于abc,结果是:{'abd' < 'abc'}")
# # a 比较 ab
# print(f"a小于ab，结果是:{'a' > 'b'}")
# # a 比较 A
# print(f"a大于A,结果是:{'a' > 'A'}")
# #  key1 比较 key2
# print(f"key1小于key2，结果是:{'key1' < 'key2'}")
# 第三章

# print(f"Belinda大于Olivia,结果是：{'Belinda '> 'Olivia'}")
# print(f"B大于O, 结果是：{'B' > 'O'}")
# print(f"王艳琳大于余江南, 结果是{'王艳琳' >  '余江南'}")

# 布尔类型和比较运算符
# 布尔类型 bool
# 布尔（bool）表达现实生活中的逻辑，即真和假
# • True表示真
# • False表示假 。
# True本质上是一个数字记作1，False记作0
# 布尔类型也是字面量，也可以用变量存储
# 定义变量存储布尔类型的数据
# 布尔字面量 True False
# 布尔变量存储
# bool_1 = True
# bool_2 = False
# print(f"bool_1变量的内容是:{bool_1},类型是:{type(bool_1)}")
# print(f"bool_2变量的内容是:{bool_2},类型是:{type(bool_2)}")
# 比较运算符
# 布尔类型的数据，不仅可以通过定义得到，也可以通过比较运算符进行内容比较得到。
# 比较运算的表达式返回值是布尔类型

# 比较运算符的使用
# ==,!=,>,<,>=,<=,
# 演示进行内容的相等比较
# num1 = 10
# num2 = 10
# print(f"10 == 10的结果是:{num1==num2}")
# print(f"10 == 10的结果是:{num1!=num2}")
# num1 = 10
# num2 = 15
# print(f"10 > 15的结果是:{num1 > num2}")
# print(f"10 < 15的结果是:{num1 < num2}")
# num1 = 20
# num2 = 10
# print(f"20 >= 10的结果是:{num1 >= num2}")
# print(f"20 <= 10的结果是:{num1 <= num2}")

# num = 10
# num1 = 10
# print(f"num等于num1, 结果是：{num == num1}")
# print(f"num不等于num1,结果是：{num != num1}")
# num2 =10
# num3=15
# print(f"num2大于num3, 结果是：{num2 > num3}")
# print(f"num2小于num3, 结果是：{num2 < num3}")
# num4 = 10
# num5 =20
# print(f"num4大于等于num5, 结果是：{num4 >= num5}")
# print(f"num4小于等于num5, 结果是:{num4 <= num5}")

# if语句的基本格式
# if 要判断的条件：
#    条件成立时，要做的事情
# 归属于if判断的代码语句块，需在前方填充4个空格缩进
# Python通过缩进判断代码块的归属关系。
# age = 30
# if age >=18:
#     print("我已经成年了")
#     print("即将步入大学生活")
# print("时间过的真快")
#  if语句的注意事项
# • 判断条件的结果一定要是布尔类型
# • 不要忘记判断条件后的： 引号
# • 归属于 if 语句的代码块，需在前方填充 4 个空格缩进
# 作业
# print("欢迎你来到游乐园,儿童免费,成人收费")
# age  = int(input("请输入年龄:"))
# if age > 18:
#     print("你已成年,需要补票10元")
# print("祝你游玩愉快")

# if else 语句
# if 条件：
#     满足条件的执行语句1
#     满足条件的执行语句2
#     ...省略...
# else：
#     不满足条件的执行语句1
#     不满足条件的执行语句2
#     ...省略...

# if else的组合判断语句
# age = int(input("请输入年龄:"))
# if age >= 18:
#     print("你已成年,需要补票10元")
# else:
#     print("你未成年,可以免费游玩")
# print("祝你游玩愉快")

# • if 和其代码块，条件满足时执行
# • else 搭配 if 的判断条件，当不满足的时候执行
#  if else语句的注意事项：
# • else 不需要判断条件，当 if 的条件不满足时， else 执行
# • else 的代码块，同样要 4 个空格作为缩进

# if elif else语句
# 使用场景：某些场景下，判断条件不止一个，可能有多个。
# if 条件一：
#     满足条件一的执行语句1
#     满足条件一的执行语句2
#     ...省略...
# elif 条件二：
#     满足条件二的执行语句1
#     满足条件二的执行语句2
#     ...省略...
# elif 条件三：
#     满足条件三的执行语句1
#     满足条件三的执行语句2
#     ...省略...
# else：
#     不满足条件的执行语句1
#     不满足条件的执行语句2
#     ...省略...
# 演示if elif else 多条件判断语句
# height = int(input("请输入身高(cm):"))
# vip_level = int(input("请输入你VIP等级(1-5):"))
# day = int(input("请输入今天的日期(1-30):"))
#通过if判断，可以使用多条件判断
#第一个条件就是if
# if height < 120:
#     print("身高小于120cm,可以免费使用。")
# elif vip_level >3:
#     print("vip级别大于3，可以免费游玩。")
# elif day == 1:
#     print("今天是号免费日，可以免费游玩。")
# else:
#     print("所有条件不满足,需要购票10元。")
# print("祝你游玩愉快")
# 注意事项
# • elif 可以写多个
# • 判断是互斥且有序的，上一个满足后面的就不会判断了
# • 可以在条件判断中，直接写 input 语句，节省代码量

# 判断语句的嵌套
# 语法格式:
# if  条件一：
#     条件一满足时的执行语句1
#     条件一满足时的执行语句2
#     if 条件二：
#         条件二满足时的执行语句1
#         条件二满足时的执行语句2
# 第二个if，属于第一个if内，只有第一个if满足条件，才会执行第二个if
# 嵌套的关键点
# 嵌套的关键点在于：空格缩进
# 通过空格缩进，来决定语句之间的：层次关系
# print("欢迎来到游乐园")
# if int(input("输入你的身高:")) > 120:
#     print("你的身高大于120cm,不可以免费")
#     print("不过如果你的vip等级高于3,可以免费游玩")
#     if int(input("请告诉我你的vip账号级别:")) > 3:
#         print("你的vip等级大于3,可以免费游玩。")
#     else:
#         print("Sorry，你需要补票10元.")
# else:
#     print("欢迎你小朋友,可以免费游玩。")

# while循环
# while循环的基础语法
# while 条件：
#     执行语句1
#     执行语句2
#     ...省略...
#  每次进入循环后，将执行语句全部执行完毕后再次来到判断，如果条件依然成立，则继续进入循环，以此类推，直到条件不成立，跳出循环
# 注意事项：
# • 条件需提供布尔类型结果， True 继续， False 停止
# • 空格缩进不能忘
# • 请规划好循环终止条件，否则将无限循环
# i = 0
# while i < 5:
#     print("你好Alan")
#     i += 1
# print(i)
# 作业：
# 演示while循环基础练习题：求1-100的和
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(f"1-100的和是：{sum}")

# while循环的嵌套
# 和判断语句的嵌套类似，这里不再长篇介绍
# i = 1
# while i < 3:
#     print(f"今天是第{i}天,准备考试")
#     j = 1
#     while j<=4:
#         print(f"刷题第{j}套")
#         j += 1
#     print("今天真难")
#     i += 1
# print(f"坚持到第{i - 1}天,终于成功")

# 补充知识print
# 默认情况下print语句输出内容会自动换行：
# print("Hello")
# print("World")
# 要求实现输出不换行的功能
# print("hello",end='')
# print("world",end='')
# 制表符\t,效果等同于在键盘上按下:tab键，可以让多行字符串进行对齐
# print("Hello World")
# print("Alan best")
# print("Hello\t World")
# print("Alan\t best")

# 定义外层循环的控制变量
# i = 1
# while i <= 9:
#     #定义内层循环的控制变量
#     j = 1
#     while i >= j:
#         #内层循环的print语句，不要换行，通过\t制表符进行对齐
#         print(f"{j} * {i} = {j*i}\t",end='')
#         j += 1
#     print()
#     i += 1
# 注意事项
# • 注意条件的控制，避免无限循环
# • 多层嵌套，主要空格缩进来确定层次关系

#  for循环
# ！！！注意！！！
# python中的for循环与C语言中的for循环差别巨大，请勿混淆
# for循环的语法格式
# for 临时变量 in 待处理数据集 :
#    循环满足条件时执行的代码
# 从待处理数据集中：逐个取出数据，赋值给临时变量
# 定义字符串name
# name = "itCSDN"
# # for循环处理字符串
# for x in name:
#        print(x)
# 可以看出，for循环是将字符串的内容：依次取出
# 所以，for循环也被称之为：遍历循环
# 同while循环不同，for循环是无法定义循环条件的。
# 只能从被处理的数据集中，依次取出内容进行处理。
# 所以，理论上讲，Python的for循环无法构建无限循环（被处理的数据集不可能无限大）
# •要注意，循环内的语句，需要有空格缩进
# 作业
# 统计如下字符串中，有多少个字母a
# name = "itheima is a brand of itcast"
# count = 0
# for i in name:
#     if i == "a":
#         count += 1
# print(f"被统计的字符串有{count}个a")

# range语句
# for 临时变量 in （可迭代对象）：
#     循环满足条件时执行的代码
# 可迭代类型是指：其内容可以以个个依次取出的一种类型，包括字符串，列表，元组，字典，集合。
# for循环语句，本质上是遍历：可迭代对象。
# 尽管除字符串外，其它可迭代类型目前没学习到，但不妨碍我们通过学习range语句，获得一个简单的数字序列（可迭代类型的一种）。
# 语法1： range(num)
# for x in range(10):
#     print(x)
# 获取一个从0开始，到num结束的数字序列（不含num本身）
# 如range(5)取得的数据是：[0, 1, 2, 3, 4]
# 语法2：range(num1,num2)
# for x in range(5,10):
#     print(x)
# 获得一个从num1开始，到num2结束的数字序列（不含num2本身）
# 如，range(5, 10)取得的数据是：[5, 6, 7, 8, 9]
# 语法3： range(num1,num2,step)
# for x in range(5,10,2):
#     print(x)
# 获得一个从num1开始，到num2结束的数字序列（不含num2本身）
# 数字之间的步长，以step为准（step默认为1）
# 如，range(5, 10, 2)取得的数据是：[5, 7, 9]
# print("输出7内的偶数")
# for i in range(0,7,2):
#     print(i)

#  变量的作用域
# 变量的作用域指变量的有效范围
# 1. for循环中的变量叫做临时变量，其作用域限定为：循环内
# 2. 这种限定：
# • 是编程规范的限定，而非强制限定.
# • 不遵守也能正常运行，但是不建议这样做.
# • 如需访问临时变量，可以预先在循环外定义它.

# 如果在for循环外部访问临时变量：
# • 实际上是可以访问到的
# • 在编程规范上，是不允许、不建议这么做的
# 演示for x循环临时变量的作用域
# 如需访问临时变量，可以预先在循环外定义它
# i = 0
# for i in range(5):
#     print(i)
# print(i)

# for循环的嵌套
# for循环嵌套模式与while循环嵌套以及判断语句的嵌套都类似，注意事项如下：
# • 需要注意缩进，嵌套 for 循环同样通过缩进确定层次关系
# • for 循环和 while 循环可以相互嵌套使用
# for i in range(1,8):
#     print(f"今天是备考的第{i}天")
#     for j in range(1,5):
#         print(f"今天刷了第{j}套题")
#     print(f"今天的任务完成")
# print(f"第{i}天,进入考场")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {j*i}\t",end='')
#     print()

# continue 和 break
# Python提供continue和break关键字用以对循环进行临时跳过和直接结束
# 当continue出现在嵌套循环中时，continue关键字只可以控制：它所在的循环临时中断
# 演示循环中断语句contine
# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")
# for i in range(1,4):
#     print(f"第{i}天：今晚的晚霞很漂亮")
#     for j in range(5,7):
#         print("今天还是去咖啡店买点面包吧")
#         if j == 6:
#             continue
#         print(f"下午{j}点了，晚风吹拂")
# 可以看到，j == 6时，下面的print语句始终没有执行，而是跳了过去继续循环

# 演示循环中语句break
# break
# break关键字用于：直接结束所在循环
# break可以用于：for循环和while循环，效果一致
# 当break出现在嵌套循环中时，break关键字同样只可以控制：它所在的循环永久中断
# for i in range(1,5):
#     if i == 3 :
#         break
#     print(i)
# print("结束了")
# 练习案例：发工资
# import random
# money = 10000
# for i in range(1,21):
#     score = random.randint(1,10)
#     if score < 5:
#         print(f"员工{i}绩效分{score},不满足，不发工资下一位")
#         continue
#         #判断余额是否充足
#     if money > 0:
#         money = money - 1000
#         print(f"员工{i}绩效分{score},满足条件发放工资1000,公司账户余额:{money}")
#     else:
#         print(f"余额不足公司账户余额:{money},不发工资了")
#         break
# print(f"工资发完了")

# 函数：是组织好的，可重复使用的，用来实现特定功能的代码段。
#  我们使用过的：input()、print()、str()、int()等都是Python的内置函数
# 作用：1.将功能封装在函数内，可供随时随地重复利用
#      2.提高代码的复用性，减少重复代码，提高开发效率
# 不使用python的内置函数len(),完成字符串长度的计算
# str1 = "python"
# str2 = "Alan is  the best student"
# count = 0
# for i in str1:
#     print(i,end='')
#     count +=1
# print(f"字符串{str1}的长度是:{count}")
# count = 0
# for i in str2:
#     print(i,end='')
#     count +=1
# print(f"字符串{str2}的长度是:{count}")
# 可以使用函数优化这个过程
# def my_len(data):
#     count = 0
#     for i in data:
#         count+=1
#     print(f"字符串{data}的长度是{count}")
# my_len(str1)
# my_len(str2)

# 函数的定义语法：
# def 函数名(传入参数)：
#     函数体
#     return 返回值
#  函数的调用：
# 函数名(参数)
#  注意事项：
# ① 参数如不需要，可以省略
# ② 返回值如不需要，可以省略
# ③ 函数必须先定义后使用
# 定义一个函数，输出相关信息
# def say_hi():
#     print("我是Alan,东软计算机学院")
# #调用函数，让调用的函数开始工作
# say_hi()
# 作业：
# def check():
#     print("欢迎来到东软学院")
# check()

# 函数的参数
# 传入参数的数量是不受限制的。
# • 可以不使用参数
# • 也可以仅使用 任意 N 个参数
# 定义两个数相加的函数，通过参数接收被计算的两个数字
# def add(x,y):
#     result = x + y
#     print(f"{x} + {y} 的结果是: {result}")
# add(5,6)
#  函数定义中，提供的 x 和 y ，称之为：形式参数（形参），表示函数声明将要使用 2 个参数
# • 参数之间使用逗号进行分隔
# • 函数调用中，提供的 5 和 6 ，称之为：实际参数（实参），表示函数执行时真正使用的参数值
# • 传入的时候，按照顺序传入数据，使用逗号分隔
# 总结：
# •函数定义中的参数，称之为形式参数
# •函数调用中的参数，称之为实际参数
# •函数的参数数量不限，使用逗号分隔开
# •传入参数的时候，要和形式参数一一对应，逗号隔开

#  函数的返回值
#  1.return 返回值
# 什么是函数的返回值: 函数在执行完成后，返回给调用者的结果
#  返回值的应用语法：
#  使用关键字：return 来返回结果
#  然后可以用变量来接收这个结果  变量 = 函数（参数）
#  注意事项：
# 函数体在遇到 return后就结束了，所以写在return后的代码不会执行。
# 语法格式图：
# def 函数(参数):
#     函数体
#     return 返回值
# 变量 = 函数(参数)
# def add(a,b):
#     result = a + b
#     #通过返回值,将相加的结果返回个调用者
#     return  result
# #函数的返回值，可以通过变量去接收
# r = add(5,6)
# print(r)

# 2.None类型
# None类型
# 思考：如果函数没有使用return语句返回数据，那么函数有返回值吗？ 实际上是：有的。
# Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>
# 无返回值的函数，实际上就是返回了：None这个字面量
# None表示：空的、无实际意义的意思
# 函数返回的None，就表示，这个函数没有返回什么有意义的内容。
# 也就是返回了空的意思。
# None可以主动使用return返回，效果等同于不写return语句：  return None

# 1.无return语句的函数返回值
# def hi_say():
#     print("你好鸭")
# result = hi_say()
# print(f"无return语句的函数返回值的内容是:{result}")
# print(f"无return语句的函数返回值的内容类型是:{type(result)}")

# 2.主动返回None的函数
# def hi_say():
#      print("你好鸭")
#      return None
# result = hi_say()
# print(f"无return语句的函数返回值的内容是:{result}")
# print(f"无return语句的函数返回值的内容类型是:{type(result)}")
# 3.None用于if判断
# def check_age(age):
#     if age > 18:
#         return "Yes"
#     else:
#         return None
# result = check_age(19)
# if not result:
#     # 进入if表示resul是None值,也接收False
#     print("未成年，不能进入")
# else:
#     print("已成年，可以进入")
# 4.None用于声明无初始化内容的变量
# name = None
# None的应用场景：
# None作为一个特殊的字面量，用于表示：空、无意义，其有非常多的应用场景。
# • 用在函数无返回值上
# • 用在 if 判断上
# • 在 if 判断中， None 等同于 False
# • 一般用于在函数中主动返回 None ，配合 if 判断做相关处理
# • 用于声明无内容的变量上
# • 定义变量，但暂时不需要变量有具体值，可以用 None 来代替
# 例如：name = None

# 演示对函数进行文档说明
# 函数的说明文档
# 函数是纯代码语言，想要理解其含义，就需要一行行的去阅读理解代码，效率比较低。
# 我们可以给函数添加说明文档，辅助理解函数的作用。
# def add(x,y):
#     """
#     add函数可以接收两个参数,进行两数相加的功能
#     :param x:形参x表示相加的其中一个数字。
#     :param y:形参y表示相加的其中一个数字。
#     :return:返回值得两数相加的结果。
#     """
#     result = x + y
#     print(f"两数相加的结果是:{result}")
#     return result
# add(5,6)
# param 用于解释参数
# • :return 用于解释返回值
#        通过多行注释的形式，对函数进行说明解释
#        •内容应写在函数体之前
# 在PyCharm编写代码时，可以通过鼠标悬停，查看调用函数的说明文档

# 函数嵌套调用函数
# 函数的嵌套调用
# 所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数
# 演示嵌套调用函数
# def func_b():
#     print("---2---")
# #定义函数func_a,并在函数内部调用func_b
# def func_a():
#     print("---1---")
#     #嵌套调用fun_b
#     func_b()
#     print("---3---")
# #调用函数func_a()
# func_a()
# 如果函数A中，调用了另外一个函数B，那么先把函数B中的任务都执行完毕之后才会回到上次 函数A执行的位置
# 注：其实函数调用非常简单，和正常使用函数无太大区别，多写几段代码就明白了

# 变量的作用域
# 变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）
# 主要分为两类：局部变量和全局变量
#  1.局部变量
# 所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
# 局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量
# def testA():
#     num = 100
#     print(num)
# testA()
# print(num)
# 变量a是定义在`testA`函数内部的变量，在函数外部访问则立即报错.
#  2.全局变量
#  所谓全局变量，指的是在函数体内、外都能生效的变量
# 思考：如果有一个数据，在函数A和函数B中都要使用，该怎么办？
# 答：将这个数据存储在一个全局变量里面
# 当全局变量和局部变量发生冲突时，优先使用局部变量
# num = 100
# def testB():
#     num = 40 #局部变量
#     print(f"testB()的num值{num}")
#
# def testC():
#     num = 79 #局部变量
#     print(f"testC()的num值{num}")
# testB()
# testC()
# print(num)
# 3.global关键字，在函数内部声明变量为全局变量
# 使用 global关键字 可以在函数内部声明变量为全局变量, 如下所示
# num = 100
# def testB():
#     num = 40 #局部变量
#     print(f"testB()的num值{num}")
#
# def testC():
#     global num
#     num = 79
#     print(f"testC()的num值{num}")
# testB()#40
# testC()#79
# print(f"全局变量num = {num}")#79
# 若不声明，则num = 100 因为： 当全局变量和局部变量发生冲突时，优先使用局部变量

# 综合案例：
# 定义全局变量money name
# money = 50000
# name = None
# #要求输入姓名
# name = input("请输入你的姓名:")
# #定义查询函数
# def query(title):
#     if title:
#         print("---------咨询余额--------")
#     print(f"{name},你好，你的余额剩余:{money}元")
# def saving(newmoney):
#     global money
#     money += newmoney
#     print("---------存款--------")
#     print(f"{name}你好，你存款{newmoney}元")
#     #调用query函数查看余额
#     query(False)
# def get_money(oldmoney):
#     global money
#     money -= oldmoney
#     print("---------取款--------")
#     print(f"{name}你好，你存款{oldmoney}元")
#     # 调用query函数查看余额
#     query(False)
# def menu():
#     print(f"{name},你好，欢迎来到中国银行ATM，请选择你的操作:")
#     print("咨询余额\t [输入1]")
#     print("存款\t\t [输入2]")
#     print("取款\t\t [输入3]")
#     print("退出\t\t [输入4]")
#     option = (input("请输入你的选择:"))
#     return option
# if __name__ == '__main__':
#     while True:
#         option = menu()
#         if option == "1":
#             query(True)
#             continue
#         elif option == "2":
#             newmoney = int(input("请输入你要存款的钱:"))
#             saving(newmoney)
#             continue
#         elif option == "3":
#             oldmoney = int(input("请输入你要取款的钱:"))
#             get_money(oldmoney)
#             continue
#         else:
#             print("程序退出了")
#             break


# 数据容器
# 数据容器入门 数据容器是什么
# 什么是数据容器？一种可以存储多个元素的Python数据类型
# 学习数据容器，就是为了批量存储或批量使用多份数据
# Python中的数据容器：
# 一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
# 每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。
# 数据容器根据特点的不同，如：
# •1是否支持重复元素 •2是否可以修改 •3是否有序，等
# 分为5类，分别是：列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）


#  list 列表
# 列表的定义:列表是一种可变的、有序的数据结构，可以随时添加和删除其中的元素。
# 基本语法：
# 1.字面量
# [元素1,元素2,元素3,元素4, ...]
# 2.定义变量
# 变量名称 = [元素1,元素2,元素3,元素4, ...]
# 3.定义空变量
# 变量名称 = []
# 变量名称 = list()
# 列表内的每一个数据，称之为元素
# 以 [ ] 作为标识
# 列表内每一个元素之间用, 逗号隔开


# 演示列表：
# name1_List = ["Alan",3.14,22,True]
# print(name1_List)
# print(type(name1_List))
# 元素的数据类型没有任何限制，甚至元素也可以是列表，这样就定义了嵌套列表
# name2_List = [['red','green'],['black','white'],name1_List]
# print(name2_List)

# 列表的下标索引
# 通过下标索引，从前向后0开始，每次+1，从后向前-1开始，每次-1，
# my_list = ["Tom","Jerry","Rose"]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# for i in my_list:
#     print(i)
# 错误示范，通过下标索引取数据，一定不能超出范围
# print(my_list[3])
# 通过下标索引取出数据(倒序取出)
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# 嵌套列表时，被嵌套的列表可以看作一个元素，
# 第一个下标就是确定元素是列表[1,2,3],再用一个下标取出这个被嵌套的列表中的元素
# 取出嵌套列表的元素
# my_list = [ [1,2,3],[4,5,6]]
# print(my_list[1][1])
# 总结：
# 1. 列表的下标索引是什么？
# 列表的每一个元素，都有编号称之为下标索引
# 从前向后的方向，编号从0开始递增
# 从后向前的方向，编号从-1开始递减
# 2. 如何通过下标索引取出对应位置的元素呢？
# 列表[下标]，即可取出
# 3. 下标索引的注意事项：
# • 要注意下标索引的取值范围，超出范围无法取出元素，并且会报错
"""
演示数据容器list列表的常用操作
"""
import json
import random
import time

# mylist = ["Alan","Tony","Fancy"]
# #1.1查找某元素的列表内的下标索引
# index = mylist.index("Alan")
# print(f"Alan在列表中的下标索引值是:{index}")
# #1.2如果被查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"hello在列表中的下标索引是:{index}")
# ValueError: 'hello' is not in list
# 2.修改特定下标索引的值
# mylist[0] = "Mark"
# print(f"列表被修改后值:{mylist}")
# 3.在指定下标位置插入新元素
# 在指定下标位置插入新元素   语法：列表.insert(下标,元素)
# 在指定的下标位置，插入指定的元素，其余元素向后移动
# mylist.insert(1,"Dio")
# newlist = []
# newlist = mylist
# print(f"列表插入元素后，结果是:{newlist}")
# print(f"列表插入元素后，结果是:{mylist}")
# print(id(newlist),id(mylist))
# 4.在列表的尾部追加单个元素(追加单个对象Append object to the end of the list)
# 在列表的尾部追加 ''' 单个 ''' 元素   语法：列表.append(元素)
# newlist = ["cici","timi"]
# mylist.append(newlist)
# mylist.append("cici")
# print(f"列表追加元素后，结果是:{mylist}")
# 5.在列表的尾部追加一堆元素(增加可迭代元素(appending elements from the iterable))
# 在列表的尾部追加 ''' 一批 ''' 元素        语法：列表.extend(另一个数据容器)
# 将另一个数据容器的内容取出，依次加到列表尾部
# mylist2 = [1,2,3]
# mylist.extend(mylist2)
# print(f"列表追加元素后，结果是:{mylist}")
# 6.删除指定下标索引的元素
# mylist = ["Alan","Tony","Fancy"]
# 6.1 方法1:del 列表[下标]
# 删除列表指定下标元素   语法：del 列表[下标]
# 与pop的区别：仅仅能完成删除操作
# del mylist[1]
# print(f"列表删除元素后，结果是:{mylist}")
# #6.1 方法2:列表.pop(下标)
# # 删除指定下标元素   语法：列表.pop(下标)
# # 与del的区别：不仅能把元素删掉，还能把删除元素作为返回值去得到
# mylist = ["Alan","Tony","Fancy"]
# element = mylist.pop(2)
# print(f"列表删除元素后，结果是:{mylist}")
# print(element)
# #7.删除某元素在列表中的第一个匹配项  语法：列表.remove(元素)
# mylist = ["Alan","Fancy","Tony","Fancy"]
# mylist.remove("Fancy")
# print(f"列表使用remove后list元素结果是:{mylist}")
# #8.清空列表   语法：列表.clear()
# mylist.clear()
# print(f"列表被清空后list元素结果是:{mylist}")
# #9.统计列表内某元素的数量       语法：列表.count(元素)
# mylist = ["Alan","Fancy","Tony","Fancy"]
# count = mylist.count("Fancy")
# print(f"列表中Fancy的数量是:{count}")
# # 10查找某元素在列表中的下标索引    语法：列表.index(元素)
# mylist = ["itCSDN", "itlove", "python"]
# index = mylist.index("itlove")
# print(f"itlove在列表中的下标索引值是：{index}")
# # 11.统计列表中全部的元素数量          语法：len(列表)
# mylist = ["itCSDN", "itlove", "python"]
# count = len(mylist)
# print(f"列表的元素数量总共有：{count}个")
#  总结列表的特点：
# • 可以容纳多个元素（上限为 2**63-1 、9223372036854775807个）
# • 可以容纳不同类型的元素（混装）
# • 数据是有序存储的（有下标序号）
# • 允许重复数据存在
# • 可以修改（增加或删除元素等）
# 作业：
# list = [21,25,21,23,22,20]
# list.append(31)
# print(list)
# list2 = [29,33,30]
# list.extend(list2)
# print(list)
# first = list.pop(0)
# print(list)
# print(first)
# end = list.pop(-1)
# print(list)
# print(end)
# index = list.index(31)
# print(index)

#  列表的遍历
# 既然数据容器可以存储多个元素，那么，就会有需求从容器内依次取出元素进行操作。
# 将容器内的元素依次取出进行处理的行为，称之为：遍历、迭代。
# 列表的遍历——while循环
# index = 0
# while index < len(列表) ：
#     元素 = 列表[index]
#     对元素进行处理
#     index += 1
# def list_while_func():
#     my_list = ["Alan","Tony","Mike"]
# 循环变量通过下标索引来控制，默认0
# 每一次循环将下标索引变量+1
# 循环条件：下标索引变量 < 列表的元素数量
# 定义一个变量用来标记列表的下标
#     index = 0  #初始化为0
#     while index < len(my_list):
#         # 通过index变量去出对应下标的元素
#         element = my_list[index]
#         print(f"列表的元素：{element}")
#         index += 1
# list_while_func()
# 列表的遍历——for循环
# 对比while，for循环更加适合对列表等数据容器进行遍历。
# for 临时变量 in 数据容器 ：
#     对临时变量进行处理
# def list_for_func():
#     my_list = [1,2,3,4,5]
#     for element in my_list:
#         print(f"列表的元素：{element}")
# list_for_func()
# for循环和while对比细节：
# 在循环控制上：
# while循环可以自定义循环条件，并自行控制
# for循环不可以自定义循环条件，只可以一个个从容器内取出数据
# 在无限循环上：
# while循环可以通过条件控制做到无限循环
# for循环理论上不可以通过条件控制做到无限循环，因为被遍历的容器容量不是无限的
# 在使用场景上：
# while循环使用于任何想要的场景
# for循环使用于遍历数据容器的场景或简单的固定次数循环场景

#  tuple 元组
# 元组一旦定义完成，就不可修改
# 1.元组的定义
# 元组定义：定义元组使用小括号，且使用逗号隔开各个数据，数据可以是不同的数据类型。
# 1.定义元组字面量
# (元素，元素，......，元素)
# (1,"Hello",True)
# 2.定义元组数量
# 变量名称 = (元素，元素，...... ，元素)
# t1 = (1,"Hello",True)
# 3.定义空元组
# 变量名称 = ()          方式一
# 变量名称 = tuple()     方式二
# t2 =()
# t3 = tuple()
# print(f"t1的类型是:{type(t1)},内容是:{t1}")
# print(f"t2的类型是:{type(t2)},内容是:{t2}")
# print(f"t3的类型是:{type(t3)},内容是:{t3}")
# 定义单个元素的元组
# t4 = ("hello")
# t4 = ("hello",)
# print(f"t4的类型是:{type(t4)},内容是:{t4}")
# 元组的嵌套
# t5 = ((1,2,3),(4,5,6))
# print(f"t5的类型是:{type(t5)},内容是:{t5}")
# 下标索引取出内容
# t5 = ((1,2,3),(4,5,6))
# print(f"从嵌套元组中取出的数据是:{t5[1][2]}")
# 元组的操作：
# 1.index查找方法：
# t6 = ("Alan","Mike","John","Ben","Cherry")
# index = t6.index("Cherry")
# print(f"在元组t6中查找Cherry的下标是:{index}")
# #2.count统计方法：
# t7 = ("Alan","Mike","Ben","John","Ben","Cherry","Ben","Ben","Ben")
# count = t7.count("Ben")
# print(f"在元组t7中统计Ben的数量是:{index}")
# #3.len函数统计元组数量
# t8 = ("Alan","Mike","Ben","John","Ben","Cherry","Ben","Ben","Ben")
# num = len(t8)
# print(f"元组t8中元素数量是:{num}")
# #元组的遍历：while
# index = 0
# while index < len(t8):
#     print(f"元组的元素有:{t8[index]}")
#     #至关重要
#     index += 1
# 元组的遍历：for
# for element in t8:
#     print(f"元组的元素有:{element}")
# 元组不可修改
# 元组里面的不可修改的是不可变容器，可修改的是可变容器。
# 多数特性和list一致，不同点在于不可修改的特性。
# 但如果元组中嵌套的有列表，那么列表中的元素可以修改（列表list的本质没有改变，所以不违背元组不可以修改的原则）
# t8[0] = "cast"
# t9 = (1,2,["Alan","Tony"])
# print(f"t9的内容是:{t9}")
# t9[2][0] = "Mike"
# t9[2][1] = "John"
# print(f"t9的内容是:{t9}")
# 总结元组的特点
# • 可以容纳多个数据
# • 可以容纳不同类型的数据（混装）
# • 数据是有序存储的（下标索引）
# • 允许重复数据存在
# • 不可以修改 （增加或删除元素等）
# • 支持for循环

# 演示以数据容器的角色，学习字符串的相关操作
# str 字符串
# 字符串是字符的容器，一个字符串可以存放任意数量的字符。
# 同元组一样，字符串是一个：无法修改的数据容器
# 和其它容器如：列表、元组一样，字符串也可以通过下标进行访问
# • 从前向后，下标从 0 开始
# • 从后向前，下标从 -1 开始
# my_str = "itheima and itcast"
# 字符串的下标索引   语法：字符串[下标]
# value = my_str[2]
# value2 = my_str[-3]
# print(f"从字符串{my_str}去下标为2的元素的值是:{value}\n取下标为-3的元素的值是:{value2}")
# #修改字符串 字符串本质上只读不能修改
# # my_str[2] = "H"
# # print(my_str)
# #index方法     语法：字符串.index(字符串)
# value3 = my_str.index("and")
# print(f"字符串{my_str}中查找and,其起始下标是:{value3}")
# #replace方法  将字符串1替换为字符串2  字符串.replace(字符串1,字符串2)
# new_my_str = my_str.replace("it","this")
# print(f"字符串{my_str},进行替换后得到:{new_my_str}")
# #splist方法 按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 语法：字符串.spilt(分隔符字符串)
# 注意：字符串本身不变，而是得到了一个新的列表对象
# my_str = "hello python itheima itcast"
# my_str_list = my_str.split(" ")
# print(f"字符串{my_str}进行split切割后得到:{my_str_list},类型是:{type(my_str_list)}")
# strip方法 字符串的规整操作(移除首尾的空格和换行符或指定字符串)
# 语法1：字符串.strip()        不传入参数时，去除首尾空格
# my_str = "  itheima and itcast  "
# new_my_str = my_str.strip() #默认去除首尾空格
# print(f"字符串{my_str}被strip后结果:{new_my_str}")
# my_str = "12itheima and itcast21"
# new_my_str = my_str.strip("12")
# print(f"字符串{my_str}被strip后结果:{new_my_str}")
# new_my_str1 = my_str.rstrip("12")
# print(f"字符串{my_str}被rstrip后结果:{new_my_str1}")
# new_my_str2 = my_str.lstrip("12")
# print(f"字符串{my_str}被lstrip后结果:{new_my_str2}")
# 统计字符串中某字符串出现的次数，count()   语法：字符串.count(字符串)
# my_str = "itheima and itcast"
# count = my_str.count("it")
# print(f"字符串{my_str}中it出现的次数是:{count}")
# 统计字符串的长度，len()     语法：len(字符串)
# length = len(my_str)
# print(f"字符串{my_str}的长度是:{length}")
# 字符串循环
# my_str = "itheima and itcast"
# index = 0
# while index < len(my_str):
#     print(my_str[index])
#     index += 1
# for element in my_str:
#     print(element)
#  总结字符串的特点
# 作为数据容器，字符串有如下特点：
#
# • 只可以存储字符串
# • 长度任意（取决于内存大小）
# • 支持下标索引
# • 允许重复字符串存在
# • 不可以修改 （增加或删除元素等）
# • 支持for循环
# 作业：
# str = "itheima itcast boxuegu"
# count = str.count("it")
# print(f"字符串{str}中有:{count}个it字符")
# new_str = str.replace(" ", "|")
# print(f"字符串{str},被替换空格后，结果：{new_str}")
# new_str1 = new_str.split("|")
# print(f"字符串{new_str},按照|分隔后，得到：{new_str1}")

# 数据容器的切片
# 序列是指：内容连续、有序，可使用下标索引的一类数据容器
# 列表、元组、字符串，均可以可以视为序列。
# 序列的常用操作——切片
# 序列支持切片，即：列表、元组、字符串，均支持进行切片操作
# 切片：从一个序列中，取出一个子序列
# 语法：序列[起始下标:结束下标:步长]
# 表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列：
# • 起始下标表示从何处开始，可以留空，留空视作从头开始
# • 结束下标（不含）表示何处结束，可以留空，留空视作截取到结尾
# • 步长表示，依次取元素的间隔
# • 步长 1 表示，一个个取元素
# • 步长 2 表示，每次跳过 1 个元素取
# • 步长 N 表示，每次跳过 N-1 个元素取
# • 步长为负数表示，反向取（注意，起始下标和结束下标也要反向标记）
# 注意，此操作不会影响序列本身，而是会得到一个新的序列（列表、元组、字符串）

# #对list进行切片，从1开始，4结束，步长为1
# my_list = [0,1,2,3,4,5,6,7,8,9]
# result1 = my_list[1:4]
# print(f"结果1:{result1}")
# #对tuple进行切片，从头开始，到最后结束，步长为1
# my_tuple = (0,1,2,3,4,5,6,7,8)
# result2 = my_tuple[:]
# print(f"结果2:{result2}")
# #对str进行切片，从头开始，到最后结束，步长为2
# my_str = "0123456"
# result3 = my_str[::2]
# print(f"结果3:{result3}")
# #对str进行切片，从头开始，到最后结束，步长为-1
# my_str1 = "0123456"
# result4 = my_str[::-1]
# print(f"结果3:{result4}")
# #对tuple进行切片，从头开始，到最后结束，步长为-2
# my_tuple1 = (0,1,2,3,4,5,6,7,8)
# result5 = my_tuple[::-2]
# print(f"结果2:{result5}")
# #对list进行切片，从8开始，1结束，步长为-2
# my_list1 = [0,1,2,3,4,5,6,7,8,9]
# result6 = my_list[8:1:-2]
# print(f"结果1:{result6}")
# 可以看到，这个操作对列表、元组、字符串是通用的
# 同时非常灵活，根据需求，起始位置，结束位置，步长（正反序）都是可以自行控制的
# 作业：需求取出man
# my_str = "dlrow eht ni nam tseb eht si nalA"
# #倒序字符串，切片取出
# new_str = my_str[-18:-21:-1]
# print(new_str)
# #切片取出,然后倒序
# # new_str1 = my_str[13:16]
# # print(new_str1[::-1]) #或
# print(my_str[13:16][::-1])
# #split分隔，replace替换空格，倒序字符串
# # new_str2 = my_str.split()
# # new_str3 = new_str2[3]
# # print(new_str3[::-1]) #或
# print(my_str.split()[3][::-1])

# 集合
# set 集合
# 集合的特点
# • 集合内不允许重复元素（去重）
# • 集合内元素是无序的（不支持下标索引）
# 1.集合基本定义语法：
# 1.定义集合字面量
# {元素,元素,元素,元素,元素,.....,元素}
# {"Alan","Tony","MiKe","John","Alan","Tony"}
# 2.定义集合变量
# 变量名称 = {元素,元素,元素,元素,元素,.....,元素}
# my_set = {"Alan","Tony","MiKe","John","Alan","Tony"} #去重复元素
# print(f"my_set的内容是:{my_set},类型是:{type(my_set)}")
# 3.定义空集合
# 变量名称 = set()
# my_set_empty = set()
# print(f"my_set_empty的内容是:{my_set_empty},类型是:{type(my_set_empty)}")
# 2.添加元素 集合.add(元素)
# 注意1：当集合本身就含有被添加的元素时，则添加无效（去重）
# 注意2：因为集合本身没有顺序，所以被添加元素位置随机
# my_set = {"Alan","Tony","Mike","John","Alan","Tony"}
# my_set.add("Python")
# print(f"my_set添加元素后的结果是:{my_set}")
# 3.移除元素 集合.remove(元素) 不会有返回值
# my_set.remove("John")
# print(f"my_set移除元素后的结果是:{my_set}")
# 4.从集合中随机取出一个元素，原集合此元素会被删除     语法：集合.pop() 有返回值element
# element = my_set.pop()
# print(f"my_set随机取出元素后的结果是:{my_set}")
# print(element)
# 5.清空集合  集合.clear()
# my_set.clear()
# print(f"my_set清空元素后的结果是:{my_set}")
# 6.取两个集合的差集（得到一个新集合）    语法：集合1.difference(集合2)
# set1 = {1,2,3}
# set2 = {1,5,6}
# set3 =set1.difference(set2)
# print(f"set1是:{set1}\nset2是:{set2}\nset3是:{set3}")
# 7.消除两个集合的差集，集合1被修改，集合2不变     语法：集合1.difference_update(集合2)
# set1.difference_update(set2)
# print(f"消除差集后，set1结果：{set1}\nset2结果:{set2}")
# 8.得到一个新的集合，内含两个集合的所有元素，原有的两个集合不变      语法：集合1.union(集合2)
# set4 = set1.union(set2)
# print(f"set1是:{set1}\nset2是:{set2}")
# print(f"两集合合并结果是：{set4}")
# 9.统计集合元素数量 len()
# set5 = {1,2,3,4,5,6}
# set6 ={1,2,3,4,5,6,1,2,3,4,5,6}
# print(f"set5集合内的元素数量有:{len(set5)}")
# print(f"set6集合内的元素数量有:{len(set6)}")
# 10.集合的遍历
# 集合不支持下标索引，不能用while循环
# set1 = {1,2,3,4,5}
# for element in set1:
# print(f"集合set1的元素有:{element}")
# 作业：
# my_list = ["Alan","Mike","Tony","Fancy","Mark","Mike","Tony","Fancy","Mark"]
# #定义一个空集合
# my_set = set()
# #通过for循环变量列表
# for element in my_list:
#     my_set.add(element)
# #打印结果
# print(my_set)
#  集合的特点
# 经过上述对集合的学习，可以总结出集合有如下特点：
# • 可以容纳多个数据
# • 可以容纳不同类型的数据（混装）
# • 数据是无序存储的（不支持下标索引）
# • 不允许重复数据存在
# • 可以修改 （增加或删除元素等）
# • 支持for循环

# 字典
# 字典的定义
# 通过 key 找出对应的 value
# 字典的定义，同样使用{}，不过存储的元素是一个个的：键值对，如下语法：
# • 使用 {} 存储原始，每一个元素是一个键值对
# • 每一个键值对包含 Key 和 Value （用冒号分隔）
# • 键值对之间使用逗号分隔  键值对定义 key ：value 三者结合被称为键值对
# • Key 和 Value 可以是任意类型的数据（ key 不可为字典）
# • Key 不可重复，重复会对原有数据覆盖
# •字典不可用下标索引，而是通过Key检索Value
# 定义字典字面量
# {key:value,key:value,.......key:value}
# {"name":"Alan","age": 18,"sex":"男"}
# 定义字典变量
# my_dict  = {key:value,key:value,.......key:value}
# my_dict1 = {"name":"Alan","age": 18,"sex":"男"}
# 定义空字典
# my_dict = {}
# my_dict = dict()
# my_dict2 = {}
# my_dict3 = dict()
# print(f"字典1的内容是：{my_dict1}，类型是:{type(my_dict1)}")
# print(f"字典2的内容是：{my_dict2}，类型是:{type(my_dict2)}")
# print(f"字典3的内容是：{my_dict3}，类型是:{type(my_dict3)}")
# 定义重复Key的字典
# my_dict1 = {"name":"Alan","age": 18,"sex":"男","name":"kai"}
# print(f"my_dict1重复Key的字典是:{my_dict1}")
# 从字典中基于Key获取Value
# 字典同集合一样，不可以使用下标索引
# 但是字典可以通过Key值来取得对应的Value
# my_dict1 = {"name":"Alan","age": 18,"sex":"男"}
# age = my_dict1["age"]
# print(f"Alan的年龄是:{age}")
# 定义嵌套字典
# 字典的Key和Value可以是任意数据类型（Key不可为字典）
# 那么，就表明，字典是可以嵌套的
# 定义嵌套字典
# stu_score_dict = {  # 回车符对字典间的元素无影响
#        "王力宏": {
#         "语文": 77,
#         "数学": 66,
#         "英语": 33
#     }, "周杰伦": {
#         "语文": 88,
#         "数学": 86,
#         "英语": 55
#     }, "林俊杰": {
#         "语文": 99,
#         "数学": 96,
#         "英语": 66
#     }
# }
# print(f"学生的考试信息是：{stu_score_dict}")
# # 从嵌套字典中获取数据
# # 看一下周杰伦的语文信息
# score1 = stu_score_dict["周杰伦"]["语文"]
# print(f"周杰伦的语文分数是：{score1}")
# score2 = stu_score_dict["林俊杰"]["英语"]
# print(f"林俊杰的英语分数是：{score2}")
# 演示字典常用操作
# my_dict = {"周杰伦":99,"林俊杰":88,"张学友":77}
# print(f"字典元素结果是:{my_dict}")
# 新增元素 字典[key] = value
# my_dict["张信哲"] = 66
# print(f"字典经过新增元素后结果是:{my_dict}")
# 更新元素 字典[key] = value
# my_dict["周杰伦"] = 44
# print(f"字典经过更新元素后结果是:{my_dict}")
# 删除元素 字典.pop()
# score = my_dict.pop("周杰伦")
# print(f"字典中被移除了一个元素结果是:{my_dict},移除的值为:{score}")
# 清空字典 字典.clear()
# my_dict.clear()
# print(f"字典中被清空，内容是:{my_dict}")
# 获取全部的Key
# 方法1：通过获取到全部的key来完成遍历
# my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}
# keys = my_dict.keys()
# print(f"字典的全部keys是：{keys}")
# # 遍历字典
# # 方法1：通过获取到全部的key来完成遍历
# for key in keys:
#     print(f"字典的key是:{key}")
#     print(f"字典的value是：{my_dict[key]}")
# # 方法2：直接对字典进行for循环，每一次循环都是直接得到key
# my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}
# for key in my_dict:
#     print(f"字典的key是:{key}")
#     print(f"字典的value是：{my_dict[key]}")
# 统计字典元素数量 len()
# length = len(my_dict)
# print(length)
# 字典的特点：
# • 可以容纳多个数据
# • 可以容纳不同类型的数据
# • 每一份数据是 KeyValue 键值对
# • 可以通过 Key 获取到 Value ， Key 不可重复（重复会覆盖）
# • 不支持下标索引
# • 可以修改 （增加或删除更新元素等）
# • 支持for循环，不支持 while 循环
# 作业：
# 用字典来组织数据
# info_dict = {
#     "Alan":{"age":20,"salary":1200,"college":"计算机学院","department":1},
#     "Tony":{"age":18,"salary":2400,"college":"商管学院","department":2},
#     "Mike":{"age":25,"salary":5200,"college":"外国语学院","department":1},
#     "Ben":{"age":23,"salary":7200,"college":"国际教育学院","department":4},
#     "John":{"age":22,"salary":8200,"college":"sovo学院","department":5},
# }
# #用for循环变量字典
# for key in info_dict:
#     print(f"员工表:{key}\t:{info_dict[key]}")
# for name in info_dict:
# # if条件判断符合条件人员
#     if info_dict[name]["department"] == 1:
#         #获取到学生的信息字典
#         Student_info_dict = info_dict[name]
#         #修改学生的个人信息
#         Student_info_dict["department"] += 1  #级别+1
#         Student_info_dict["age"] += 1         #年龄+1
#         Student_info_dict["salary"] += 1000  #工资+1000
#         #将学生的信息更新到info_dict
#         info_dict[name] = Student_info_dict
#     elif info_dict[name]["department"] == 2:
#         Student_info_dict = info_dict[name]
#         Student_info_dict["department"] += 1  # 级别+1
#         Student_info_dict["age"] += 2  # 年龄+1
#         Student_info_dict["salary"] += 2000  # 工资+1000
#     elif info_dict[name]["department"] == 3:
#         Student_info_dict = info_dict[name]
#         Student_info_dict["department"] += 1  # 级别+1
#         Student_info_dict["age"] += 4  # 年龄+1
#         Student_info_dict["salary"] += 4000  # 工资+1000
#     elif info_dict[name]["department"] == 4:
#         Student_info_dict = info_dict[name]
#         Student_info_dict["department"] += 1  # 级别+1
#         Student_info_dict["age"] += 2  # 年龄+1
#         Student_info_dict["salary"] += 2000  # 工资+1000
#     elif info_dict[name]["department"] == 5:
#         Student_info_dict = info_dict[name]
#         Student_info_dict["department"] += 1  # 级别+1
#         Student_info_dict["age"] += 5  # 年龄+1
#         Student_info_dict["salary"] += 5000  # 工资+1000
#     else:
#         print("无法修改")
# print(f"修改之后的学生表:{info_dict}")

# 数据容器的通用操作
# 基于各类数据容器的特点，它们的应用场景如下：
# • 列表：一批数据，可修改、可重复的存储 场景
# • 元组：一批数据，不可修改、可重复的存储 场景
# • 字符串：一串字符串的存储 场景
# • 集合：一批数据，去重存储 场景
# • 字典：一批数据，可用 Key 检索 Value 的存储场景
# • 列表使用： []
# • 元组使用： ()
# • 字符串使用：""
# • 集合使用： {}
# •字典使用：{}和键值对

# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "abcdefg"
# my_set = {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
# len元素个数
# print(f"列表元素的个数有：{len(my_list)}")
# print(f"元组元素的个数有：{len(my_tuple)}")
# print(f"字符串元素的个数有：{len(my_str)}")
# print(f"集合元素的个数有：{len(my_set)}")
# print(f"字典元素的个数有：{len(my_dict)}")
# 按住shift + alt + 拖动鼠标 选中同一列

# max的最大元素  容器内最大元素  语法：max(数据容器名)
# print(f"列表元素的最大值： {max(my_list)}")
# print(f"元组元素的最大值： {max(my_tuple)}")
# print(f"字符串元素的最大值:{max(my_str)}")
# print(f"集合元素的最大值： {max(my_set)}")
# print(f"字典元素的最大值： {max(my_dict)}")

# min的最小元素  容器内最小元素  语法：min(数据容器名)
# print(f"列表元素的最小值： {min(my_list)}")
# print(f"元组元素的最小值： {min(my_tuple)}")
# print(f"字符串元素的最小值:{min(my_str)}")
# print(f"集合元素的最小值： {min(my_set)}")
# 字典转列表时会丢掉value值
# print(f"字典元素的最小值： {min(my_dict)}")

# 类型转换：数据容器转列表    语法：list(数据容器名)
# print(f"列表转列表的结果是:{list(my_list)}")
# print(f"元组转列表的结果是:{list(my_tuple)}")
# print(f"字符串转列表的结果是:{list(my_str)}")
# print(f"集合转列表的结果是:{list(my_set)}")
# print(f"字典转列表的结果是:{list(my_dict)}")
# 类型转换： 数据容器转元组   语法：tuple(数据容器名)
# print(f"列表转元组的结果是:{tuple(my_list)}")
# print(f"元组转元组的结果是:{tuple(my_tuple)}")
# print(f"字符串转元组的结果是:{tuple(my_str)}")
# print(f"集合转元组的结果是:{tuple(my_set)}")
# 字典转元组时会丢掉value值
# print(f"字典转元组的结果是:{tuple(my_dict)}")
# 类型转换： 数据容器转字符串  语法：str(数据容器名)
# print(f"列表转字符串的结果是:{str(my_list)}类型是:{type(str(my_list))}")
# print(f"元组转字符串的结果是:{str(my_tuple)}类型是:{type(str(my_tuple))}")
# print(f"字符串转字符串的结果是:{str(my_str)}类型是:{type(str(my_str))}")
# print(f"集合转字符串的结果是:{str(my_set)}类型是:{type(str(my_set))}")
# print(f"字典转字符串的结果是:{str(my_dict)}类型是:{type(str(my_dict))}")
# 类型转换：数据容器转集合    语法：set(数据容器名)
# print(f"列表转集合的结果是:{set(my_list)}")
# print(f"元组转集合的结果是:{set(my_tuple)}")
# print(f"字符串转集合的结果是:{set(my_str)}")
# print(f"集合转集合的结果是:{set(my_set)}")
# print(f"字典转集合的结果是:{set(my_dict)}")
# 注意:列表,元组,字符串,集合不能转字典，只能字典转字典
# 容器排序 可正序也可倒序
# my_list = [5, 4, 3, 2, 1]
# my_tuple = (4, 3, 5, 1, 2)
# my_str = "abcdefg"
# my_set = {5, 1, 2, 3, 4}
# my_dict = {"key1": 5, "key2": 2, "key3": 1, "key4": 3, "key5": 4}
# 1、正序排列  语法：sorted(数据容器名)
# print(f"列表对象的排序结果:{sorted(my_list)}")
# print(f"元组对象的排序结果:{sorted(my_tuple)}")
# print(f"字符串对象的排序结果:{sorted(my_str)}")
# print(f"集合对象的排序结果:{sorted(my_set)}")
# print(f"字典对象的排序结果:{sorted(my_dict)}")
# 2、逆序排列    语法：sorted(数据容器名, reverse=True)
# print(f"列表对象的反向排序结果: {sorted(my_list,reverse=True)}")
# print(f"元组对象的反向排序结果: {sorted(my_tuple,reverse=True)}")
# print(f"字符串对象的反向排序结果:{sorted(my_str,reverse=True)}")
# print(f"集合对象的反向排序结果:  {sorted(my_set,reverse=True)}")
# print(f"字典对象的反向排序结果: {sorted(my_dict,reverse=True)}")

# 第七章:函数进阶

# 一.函数的多个返回值
# 1.按照返回值得顺序，写对应顺序的多个变量接收即可
# 2.变量之间用逗号隔开
# 3.支持不同类型的数据return
# 例如:
# def test_return():
#     return  1,2
# x,y = test_return()
# print(x)  #结果1
# print(y)  #结果2
# 二.函数的多种传参方式
# 1.掌握位置参数
# 位置参数：调用函数时根据函数定义的参数位置来传递参数
# def user_info1(name,age,gender):
#     print(f"你的名字{name},年龄是{age},性别是:{gender}")
# user_info1('Alan',20,'男')
# 注意:传递的参数和定义的参数的顺序及格数必须一致
# 2.掌握关键字参数
# 关键字参数:函数调用时通过"键 = 值"形式传递参数
# 作用:可以让函数更加清晰，容易使用。同时也清除了参数的顺序需求.
# def user_info2(name,age,gender):
#     print(f"你的名字{name},年龄是{age},性别是:{gender}")
# 2.关键字传参
# user_info2(name='Tom',age=20,gender='男')
# #可以不按照顺序
# user_info2(age=22,gender='女',name='Tony')
# #可以和位置参数混用，位置参数必须在前。而且匹配参数顺序
# user_info2("Dio",age=22,gender='男')
# user_info2("Dio",22,gender='男')
# 注意:函数调用时，如果有位置参数时。位置参数必须在关键字参数的前面，的关键字参数之间不存在先后顺序
# 3.掌握缺省参数
# 缺省参数:也叫默认参数。用于定义函数时为参数提供默认值，调用函数时可不传该默认参数的值
# 注意:所有位置参数必须出现在默认参数前，包括函数定义和调用.
# def user_info3(name,age,gender='男'):
#     print(f"你的名字{name},年龄是{age},性别是:{gender}")
# user_info3('ZSH',20)
# user_info3('ZSH',20,'女')
# 注意:函数调用时，如果为缺省参数传值则修改默认参数值，否则使用这个默认值
# 4.掌握不定长参数
# 不定长参数：也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景。
# 作用:当调用函数时不确定参数个数时，可以使用不定长参数。
# 不定长参数的类型:
#  1.位置传递
# def user_info4(*args):
#    print(f"args的参数类型是:{type(args)},内容是:{args}")
# user_info4('Alan')
# user_info4('Alan',20)
# user_info4('Alan',20,[1,2,3,4,5])
# 注意:传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple),args是元组类型。这就是位置传递。
# 2.关键字传递
# def user_info4(**kwargs):
#     print(f"kwargs的参数类型是:{type(kwargs)},内容是:{kwargs}")
# user_info4(name = 'Alan', age = 22, gender = '男')
# 注意：参数是“键 = 值"形式的情况下，所有的”键 = 值“都会被kwargs接受，同时会根据"键 = 值"组成字典

# 三.匿名函数
# 1.函数作为参数传递
# 在前面学习都是将数据作为参数传入：数字，字符串，字典，列表，元组
# 其实函数本身也可以作为参数传令一个函数内
# 定义一个函数接收另一个函数作为传入的参数
# def test_fun(computer):
#     result = computer(2,4)
#     print(f"computer参数的类型是:{type(computer)}")
#     print(result)
# 定义一个函数准备作为参数传入另一个函数
# def computer(x,y):
#     return  x * y
# 调用,并传入的函数
# test_fun(computer) #函数computer作为参数传入到test_fun函数中使用
# test_fun需要一个函数作为参数传入，这个函数需要接收2个数字进行计算，计算逻辑由这个被传入的函数决定。
# 第二 computer函数接收两个数字对其进行计算，computer函数作为参数，传递给test function函数使用。
# 最终，test_fun()函数内部，由传入的computer函数完成对数字的计算操作。
# 所以这是一种计算逻辑的传递而非数据的传递，就这样上面的代码一样不仅可以相加相减相除等其他任何逻辑都可以进行自定义 并作为函数传入。
# 2.lambda匿名函数
# 函数的定义中
# def关键字,可以定义带有名称的函数
# lambda关键字，可以定义匿名的函数（无名称）
# 有名字的函数可以基于名字重复利用，没有名字的函数称为匿名函数只可以临时使用一次
# 匿名函数调用的语法：
# lambda 传入参数:函数体(一行代码)
# 1.lambda 是关键字,表示定义匿名函数
# 2.传入参数表示匿名函数的形式参数如X，Y表示接收两个形式参数
# 3.函数体就是函数的执行逻辑要注意只能写一行无法写多行代码
# 例子：
# 使用def和lambda定义的函数功能一致,只是lambda关键字定义的函数是匿名的无法二次使用
# def test_func(computer):
#     result = computer(2, 4)
#     print(f"computer参数的类型是:{type(computer)}")
#     print(result)
# test_func(lambda x,y :x + y)

# 第八章:文件操作
# 1.文件的编码
# 计算机只能识别0和1,那么我们丰富的文本内容如何被计算机识别?
# 使用编码技术,将内容翻译0和1存储到计算机中。
# 文件编码：即翻译的规则，记录了如何将内容翻译成二进制，如何将二进制翻译回可识别的内容
# 计算机中有许多可用的编码:
# 1.UTF-8 2.GBK(中文编码) 3.Big5(繁体字) 4.其他
# 不同的编码将内容翻译成二进制也是不同的
# 编码有许多，所以要使用正确的编码方式，才能对文件进行正确的读写操作
# 我们可以使用Windows系统自带的记事本打开文件后就能看出文件的编码是什么
# UTF-8是目前全球·通用的编码格式，除非有特殊的要求，否则一律以UTF-8格式进行文件的编码即可

# 2.文件的读取
# 1.了解文件操作的作用
# 什么是文件？
# 内存中存放的数据在计算机关机后就会消失, 倘若要长久的保存数据那么就必须要使用
# 硬盘,光盘,U盘等设备去保存数据,为了便于数据的管理和检索,就引用了文件这个概念.
# 一篇文章，一段视频，一个可执行的程序都可以被保存为一个文件，并赋予一个文件名。
# 操作系统以文件为单位管理磁盘中的数据。一般来说文件可以分为：文本文件，视频文件，音频文件，图像文件，可执行文件等多种类别 。
# 标准术语：
# 在计算机中为了管理和检索数据引入了文件的概念，为了更好的使用文件，引入了文件夹（树形文件目录）。
# 根据文件的功能不同可以将文件分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别。
# 这些文件实质上都是由一个个字节组成（0、1比特串），之所以呈现不同的形态是由文件的创建者和解释者约定的文件格式决定的。
# 例如：常见的文本文件是指能够在记事本中打开，并且能看出是一段有意义的文字的文件，即文本文件中的每个字节都是一个可见字符的ASCII码。
# 另外图像、视频、可执行文件等一般被称作“二进制文件”。这些所谓的格式只是关于文件中每一部分的内容代表什么含义的一种约定，从计算机用户角度出发的一种分类。
# 但从计算机科学的角度来看，所有的文件都是由二进制位组成的，都是二进制文件，文本文件和其他二进制文件只是格式不同而已。
# 文件操作包含那些操作呢？
# 文件操作主要包含打开，关闭，读写等操作
# 步骤为：1.打开文件，2读写文件3.关闭文件
# 注意:可以只打开文件和关闭文件，不做读写操作
# 1.打开文件
# open()打开函数
# 在Python中使用open函数可以打开一个已存在的文件或者创建一个新文件,语法如下：
# open(name,mode,encoding)
# name:是要打开的目标文件名的字符串，可以包含文件所在的具体路径
# mode:设置打开文件的模式(访问模式) 只读,写入,追加,等
# encoding:编码格式(推荐使用UTF-8)
# 示例代码：
# f = open('Python.txt','r',encoding="UTF-8")
# encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
# 注意：此时的f是open函数的文件对象,对象是Python中一种特殊的数据类型,拥有属性和方法可以使用对象.属性,或对象.方法对其进行访问.后续面向对象课程会给大家进行详细的介绍
# r模式：以只读方式打开文件，文件的指针将会放在文件的开头这是默认模式。
# w模式:打开一个文件只用于写入,如果该文件已存在,则打开文件并从开头开始编译,原有内容会被删除.如果该文件不存在,创建新文件写入.
# a模式：打开一个文件用于追加，如果该文件已存在，新的内容将会被写入到已有的内容之后，如果该文件不存在，创建新文件进行写入。
# 2.读写操作相关方法
# read()方法：文件对象。read(num)
# num表示要从文件中读取的数据的长度(单位是字节)，如果没有传入num,那么就表示读取文件中所有的数据
# readlines()方法：
# readlines可以按照行的方式把整个文件的内容进行一次性的读取，并且返回的是一个列表，其中每行的数据为一个元素
# readline()方法:
# readline可以按行的方式一次读取一行的数据,并且返回的是一个字符串
# close()关闭文件对象
# 最后通过close关闭文件对象，也就是关闭对文件的占用。 如果不调用close，同时程序没有停止运行，那么这个文件将一直被Python程序占用。
# with open() 语法：
# with open("D:/computer science and technology/Python.txt","r",encoding="UTF-8") as f:
#     f.readlines()
# 通过在with open的语句块中对文件进行操作,可以在操作完成后自动关闭close文件避免遗忘掉close方法.
# 打开文件
# file = open("D:/computer science and technology/Python.txt","r",encoding="UTF-8")
# print(type(file))
# 读取文件 - read()
# print(f"读取10个字节的结果是:{file.read(10)}")
# 第一次读取read的结尾文件指针指向第10个字符，下一次再读取read会在第10个字符开始读取。
# print(f"read方法读取全部内容的结果是:\n{file.read()}")
# print("----------------------------------------------------------")
# 读取文件 - readlines()
# lines = file.readlines()  #读取文件的全部行，封装到列表中
# print(f"lines对象的类型是:{type(lines)}")
# print(f"lines对象的内容是:{lines}")
# 读取文件 - readline()
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# print(f"第一行数据line1对象的内容是:{line1},类型是{type(line1)}")
# print(f"第二行数据line2对象的内容是:{line2},类型是{type(line2)}")
# print(f"第三行数据line3对象的内容是:{line3},类型是{type(line3)}")
# for循环读取文件行
# for line in file:
#     print(f"每一行数据是:{line}")
# time.sleep(40000)
# 文件的关闭
# file.close()
# time.sleep(40000)
# with open 语法操作文件
# with open("D:/computer science and technology/Python.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据是:{line}")
# time.sleep(30000)
# 课后练习：单词计数
# 方法1：read()，读取全部内容，通过字符串count方法统计itheima单词的个数
# count = 0
# with open("D:/computer science and technology/Python.txt","r",encoding="UTF-8") as file:
#     context = file.read()
#     count = context.count("itheima")
# print(f"itheima在文件的次数是:{count}")
# 方法二:用for循环迭代读取每一行
# f = open("D:/computer science and technology/Python.txt","r",encoding="UTF-8")
# count1 = 0 #使用count变量记录
# for line in f:
#     line = line.replace("\n"," ") #将换行符替换成空格
#     #line = line.strip() #去掉开头和结尾的空格以及换行符
#     words = line.split(" ")
#     for word in words:
#         if word == "itheima":
#             count1 += 1
# print(f"itheima在文件的次数是:{count1}")
# f.close()

# 3.文件的写入
# 直接调用write，内容并没有真正写入文件，而是会累计在程序的内存中，该区域称为缓冲区
# 当调用flush的时候，内容会真正写入文件
# 这样做是为了避免频繁的操作硬盘，导致效率下降(积累一堆，一次性写入磁盘)
# write()写入内容到文件里面，
# flush()刷新内容到硬盘中
# 当文件不存在的时候，w模式会创建文件；当文件存在的时候，w模式会清空原有的内容
# 其中close方法内置flush方法
# open打开不存在的文件
# f = open("D:/computer science and technology/test.txt","w",encoding="UTF-8")
# #write写入
# f.write("Hello World!!!") #内容写入到内存中
# #flush刷新
# f.flush()
# time.sleep(20)
# #close关闭 其中close方法内置flush方法
# f.close()
# #open打开存在的文件
# f = open("D:/computer science and technology/test.txt","w",encoding="UTF-8")
# #当文件不存在时，以w的方法写入新的内容，当文件存在的时候，会将文件里面的内容全部清空，然后再写入新的内容
# f.write("AlanAlanAlan\nAlanAlanAlan")
# f.close()
# 4.文件的追加
# 注意:
# a模式，文件不存在会创建文件
# a模式，文件存在会在原有的内容最后追加写入文件
# 可以使用"\n"产生换行效果
# f = open("D:/computer science and technology/test.txt","a",encoding="UTF-8")
# f.write("学习python找Alan")
# f.close()
# f = open("D:/computer science and technology/test.txt","a",encoding="UTF-8")
# f.write("你行你就来")
# f.close()
# 5.综合案例
# 1.读取文件 2.将文件写入到bill.text.bak文件作为备份. 3.同时将文件内标记测试的数据行丢弃
# 打开文件得到文件对象，准备读取
# fr = open("D:/computer science and technology/test.txt", "r", encoding="UTF-8")
# # 打开文件得到文件对象，准备写入
# fw = open("D:/computer science and technology/test1.txt", "w", encoding="UTF-8")
# #for循环读取文件
# for line in fr:
#     line = line.strip()
#     #判断内容，将满足的内容写出
#     if line.split(",")[2] == "测试": #看每一列第二个逗号后的内容是否与该字符串匹配
#         continue
#     #将内容写出去
#     fw.write(line)
#     #由于前面对内容进行了strip()的操作，所以要手动的写出换行符
#     fw.write("\n")
# #close两个文件对象
# fr.close()
# fw.close()

# 了解异常
# 什么是异常:当检测到一个错误时，python解释器就无法继续执行了，反而出现了一些错误提示，这就是所谓的异常，也就是bug
# 异常的捕捉方法
# 为什么要捕获异常
# 要在力所能及的范围内，对可能出现的bug，进行提前准备，提前处理，这种行为称为:异常处理(捕捉异常)
# 当我们的程序遇到bug 有两种情况 1.整个程序因为一个bug停止运行， 2.对bug进行提醒整个程序继续运行
# 捕获异常的作用在于:提前假设某出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段。
# 基本捕获语法：
# 方法1:
# try:
#     可能发生称为的代码
# except:
#     如果出现异常执行的代码
# try:
#     file = open("D:/computer science and technology/abc.txt","r",encoding="UTF-8")
#     file.read()
# except:
#     print("出现的异常了,因为文件不存在，我将open方法中r模式改为w模式去打开")
#     file = open("D:/computer science and technology/abc.txt", "w", encoding="UTF-8")
#
# 方法2:捕获指定的异常
# try:
#     print(name)
#     # 1 / 0
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)
# 方法3.捕获多个异常
# try:
#     # print(name)
#     1 / 0
# except (NameError,ZeroDivisionError) as e:
#     print("出现里变量为定义或者除以0的异常")
#     print(e)
# 方法4:捕获所有异常
# try:   #(必选)
#     file = open("D:/computer science and technology/test.txt","r",encoding="UTF-8")
# except Exception as e:  #(必选) expext[异常 as 别名:]
#     print(f"出现异常了，是{e}")
# else: #else表示的是如果没有异常要执行的代码(可选)
#     print("好高兴,没有异常。")
# finally:  #finally表示无论如何是否异常都要执行的代码，例如关闭文件(可选)
#     file.close()
#     print("关闭成功")

# 异常的传递
# 异常具有传递性，当函数func01中发生异常，并且没有捕获处理这个异常的时候，异常会传递到函数func02,当func02也没有捕获处理这个异常的时候， main函数会捕获这个异常，这就是异常的传递性。
# 提示：当所有函数都没有捕获异常的时候，程序会报错。
# def func01():
#     print("这是func01开始")
#     num = 1 / 0
#     print("这是func01结束")
#
# def func02():
#     print("这是func02开始")
#     func01()
#     print("这是func02结束")
#
# def main():
#     try:
#         func02()
#     except Exception as e:
#         print(e)
#
# if __name__ == '__main__':
#     main()
# Python模块
# 什么是模块？
# Python模块(Module),是一个Python文件，以.py结尾。模块能定义函数，类，变量，模块里也能包含可执行的代码。
# 模块的作用:python中有很多不同的模块，每一个模块都可以帮助我们快速的实现一些功能
# 比如实现和时间相关的功能就可以使用time模块，我们可以认为一个模块就是一个工具包
# 每一个工具包中都有各种不同的工具提供个我们使用
# 模块就是一个python文件，模块里面有函数，类，变量，模块里也能包含可执行的代码给我们使用(导入模块去使用)
# 模块的导入方式
# [from 模块名] import [模块|类|变量|函数|*] [as 别名]
# 常见的组合形式如：
# 1.import 模块名
# 2.from 模块名 import 类，变量，方法等
# 3.from 模块名 import *
# 4.import 模块名 as 别名
# 5.from 模块名 import 功能名 as 别名
# 第一种：
# import time    #导入python内置的time模块(time.py)
# print("你好")
# time.sleep(5)
# print("hihi")
# 第二种:使用time模块的特定功能或者指定的函数，变量，类
# from time import sleep
# print("你好")
# sleep(5)
# print("hihi")
# 第三种：把模块内部的所有功能都导进来
# from time import *
# print("你好")
# sleep(5)
# print("hihi")
# 第四种:把模块内部的所有功能都导进来并给模块取别名
# 使用as个特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("hihi")
# 第五种:把模块内部的所有功能都导进来并给特定的功能取别名
# from time import sleep as sl
# print("你好")
# sl(5)
# print("hihi")
# 注意事项:
# from 可以省略，直接import即可
# as别名可以省略
# 通过.来确认层级关系
# 模块的导入一般写在代码文件的开头位置

# 自定义模块
# 1.了解如何自定义模块并使用
# Python中已经帮我们实现了很多的模块，不过有时候我们需要一些个性化的模块，这里就可以通过自定义模块实现也就是自己制作一个模块。
# 注意：每一个Python文件可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块名必须要符合标识符命名规则。
# import my_module1
# from my_module1 import test
# my_module1.test(2,3)
# test(3,4)
# 注意事项:当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能的时候，调用的是后面导入的模块的功能。因为后导入会覆盖前导入的
# from my_module1 import test
# from my_module2 import test
# test(2,6)
# 2.了解_main_变量的作用
from my_module1 import test

# 如果一个模块文件有__all__变量，使用from xxx import * 导入是，只能导入这个列表中的元素
# from my_module1 import *
# test1()        #这里只能显示test1的功能，不能显示test, test2的功能


# Python包
# 什么是Python的包？
# 物理逻辑上来看包就是一个文件夹，该文件夹下包含了一个__init__.py 文件,该文件用于包含多个块文件.
# 从逻辑上看包本质上还是模块， 相当于一个大模块。
# 包的作用：当然的模块文件越来越多的时候， 包可以帮助我们管理这些模块， 包的作用就是包含多个模块，本质上模块。
# 有__init__.py就是包，没有就是文件夹。
# 创建包的步骤：
# 1.新建包my_package
# 2.新建包内的模块:my_module01和 my_module02
# 新建包后，包内部都会自动创建__init__.py文件，这个文件控制包的导入行为
# 导入自定义的包中的模块，并使用
# 方法1：
# import my_package.my_module01
# import my_package.my_module02
#
# my_package.my_module01.info_print1()
# my_package.my_module02.info_print2()
# 方法2:
# from my_package import my_module01
# from my_package import my_module02
# my_module01.info_print1()
# my_module02.info_print2()
# 方法3：
# from my_package.my_module01 import info_print1
# from my_package.my_module02 import info_print2
# info_print1()
# info_print2()
# 导入包
# 注意:必须在__init__.py文件中添加__all__=[]用来控制导入的模块列表
# __all__针对的是from...import*这种方式, import xxx无效
# from my_package import *
# my_module01.info_print1()
# my_module02.info_print2()    #NameError: name 'my_module02' is not defined


# 安装第三方Python包
# 1.了解什么是第三方包

# 2.掌握使用pip安装第三方包
# 打开我们的命令提示符程序在里面输入：
# pip install 包名称
# pip的网络优化
# 通过网络安装，默认连接国外网站，使用国内清华大学提供的网站下载迅速
# pip install -i https://pypi.tsinghua.edu.cn/simple 包的名称

# 练习案例:
# 创建一个自定义包 名称为:my_utils
# 在包内提供两个模块
# str_util.py(字符串相关工具，内含:)
# 函数：str_reverse(s)，接受传入字符串，将字符串反转返回
# 函数：substr(s,x,y), 按照下标x和y,对字符串进行切片
# file_util.py(文件处理相关工具，内含:)
# 函数:print_file_info(file——name),接收传入文件的路径,打印文件的全部内容.
# 如果文件不存在则捕获异常 输出提示信息通过finally关闭文件对象
# 函数:append_to_file(file_name,data),接收文件路径以及传入数据，将数据追加写入到文件中
# from my_utils.str_util import *
#
# print(str_reverse("hello"))
# print(substr("sdnsnflks", 2, 10))
#
# from my_utils.file_util import *
# append_to_file("D:/computer science and technology/test.txt","Alan is handsome man")
# print_file_info("D:/computer science and technology/test.txt")

# 数据可视化之折线图可视化
# 1.json数据格式
"""
演示json数据和Python字典的相互转换
"""
# #导入json模块
# import  json
# #准备列表，列表内没一个元素都是字典，将其转换为json
# data1 = [{"name":"老王","age":16},{"name":"张三","age":20}]
# json_str1 = json.dumps(data1,ensure_ascii= False)
# #设置为False表示不用ASCII码来转换它，而是直接输出内容出去，假如是True的话，中文转换为Unicode的字符
# print(f"json_str的类型是:{type(json_str1)}\n内容是:\n{json_str1}")
# #准备一个列表，转换为json
# data2 = {"name":"Alan","address":"中国","age":22}
# json_str2 = json.dumps(data2, ensure_ascii=False)
# print(f"json_str的类型是:{type(json_str2)}\n内容是:\n{json_str2}")
# #将json的字符串转换为对应的数据类型列表
# str_1 = '[{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]'
# list = json.loads(str_1)
# print(f"list的数据类型是:{type(list)}\nlist的内容是:\n{list}")
# #将json的字符串转换为对应的数据类型字典
# str_2 = '{"name": "Alan", "address": "中国", "age": 22}'
# dict = json.loads(str_2)
# print(f"dict的数据类型是:{type(dict)}\nlist的内容是:\n{dict}")

# 2.pyecharts模块介绍

# 3.pyecharts快速入门
# 导包
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# #创建一个折线图对象
# line = Line()
# #给折线图对象添加x轴的数据
# line.add_xaxis(["中国","美国","英国"])
# #给折线图对象添加Y轴的数据
# line.add_yaxis("GDP",[30,20,10])
# #设置全局配置项set_global_opts来设置
# line.set_global_opts(
#     title_opts = TitleOpts(title = "GDP展示", pos_left = "center", pos_bottom = "1%")
#     legend_opts = LegendOpts(is_show = True)
#     toolbox_opts = ToolboxOpts(is_show = True)
#     visualMap_opts =VisualMapOptss(is_show = True)
# )
# 通过render方法，将代码生成成为图像
# line.render()

# # 4.数据处理
# import json
# f_us = open("D:/美国.txt","r",encoding="UTF-8")
# us_data = f_us.read()  #读取美国的全部内容
# f_jp = open("D:/日本.txt","r",encoding="UTF-8")
# jp_data = f_jp.read()  #读取日本的全部内容
# f_in = open("D:/印度.txt","r",encoding="UTF-8")
# in_data = f_in.read()  #读取印度的全部内容
# #去掉不会json规范的开头
# frontdata1 = "sbasbcjsbc"
# frontdata2 = "sdiuiuisdv"
# frontdata3 = "ohfewifewn"
# us_data = us_data.replace(frontdata1,"")
# jp_data = jp_data.replace(frontdata2,"")
# in_data = in_data.replace(frontdata3,"")
# #去掉不会json规范的结尾
# us_data = us_data[:-4]
# jp_data = us_data[:-8]
# in_data = us_data[:-12]
# #json转python字典
# us_dict = json.loads(us_data)
# jp_dict = json.loads(jp_data)
# in_dict = json.loads(in_data)
# print(f"该数据类型是:{type(us_dict)},内容是:{us_dict}")
# print(f"该数据类型是:{type(jp_dict)},内容是:{jp_dict}")
# print(f"该数据类型是:{type(in_dict)},内容是:{in_dict}")
# #获取trend key
# trend_data1 = us_data['data'][0]['trend']
# trend_data2 = jp_data['data'][0]['trend']
# trend_data3 = in_data['data'][0]['trend']
# print(f"该数据类型是:{type(trend_data1)},内容是:{trend_data1}")
# print(f"该数据类型是:{type(trend_data2)},内容是:{trend_data2}")
# print(f"该数据类型是:{type(trend_data3)},内容是:{trend_data3}")
# #获取日期数据，用于x轴,取2020年
# x_data1 = trend_data1['updateDate'][:314]
# x_data2 = trend_data2['updateDate'][:614]
# x_data3 = trend_data3['updateDate'][:724]
# print(x_data1)
# print(x_data2)
# print(x_data3)
# #获取确认数据，用于y轴,取2020年
# y_data1 = trend_data1['list'][0]['data']
# y_data2 = trend_data2['list'][0]['data']
# y_data3 = trend_data3['list'][0]['data']
# print(y_data1)
# print(y_data2)
# print(y_data3)
# #生成图表
# from pyecharts.chart import Chart
# line = Chart()
# line.__add( x_axis = x_data1, y_axis = y_data1)
# 5.创建折线图



# #1.设计一个类
# class Student:
#     name = None         #记录学生姓名
#     gender = None       #记录学生性别
#     nationality = None  #记录学生国籍
#     native_place = None #记录学生籍贯
#     age = None          #记录年龄
# #2.创建一个对象
# stu_1 = Student()
# #3.对象的属性赋值
# stu_1.name = "Alan"
# stu_1.gender = "男"
# stu_1.nationality = "中国"
# stu_1.native_place = "广东省"
# stu_1.age = 20
# #4.获取对象中记录的信息
# print(f"学生姓名:{stu_1.name},"
#       f"学生性别:{stu_1.gender},"
#       f"学生国籍:{stu_1.nationality},"
#       f"学生籍贯:{stu_1.native_place},"
#       f"学生年龄:{stu_1.age}")

# 定义一个带有差异方法的类
# class Student1:
#     name = None
#     def say_hi(self):
#         print(f"大家好,我是{self.name},欢迎大家多多关照")
#
#     def say_hi2(self,msg):
#         print(f"大家好,我是:{self.name},{msg}")
#
# stu1 = Student1()
# stu1.name = "Amy"
# stu1.say_hi()
# stu1.say_hi2("Tom你好呀")
#
#
# stu2 = Student1()
# stu2.name = "Tom"
# stu2.say_hi()
# stu2.say_hi2("Amy你好呀")

# 构造方法：
# class Student:
#     name = None
#     age = None
#     tel = None
#
#     def __init__(self,name,age,tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         print("Student构造方法被执行")
#
# stu1 = Student("Alandjfnd",40,"11372845610")
# print(stu1.name)
# print(stu1.age)
# print(stu1.tel)

# class Student:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# for i in range(1,11):
#     print(f"当前录入第{i}位学生信息,总共需录入10位学生信息")
#     name = input("请输入学生姓名:")
#     age = int(input("请输入学生年龄:"))
#     address = input("请输入学生地址:")
#     stu1 = Student(name, age, address)
#     print(f"学生{i}信息录入完成,信息为:学生姓名:{stu1.name},学生年龄:{stu1.age},学生地址:{stu1.address}")

#魔术方法
# class Student:
#     #__init__魔术方法
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#     #__str__魔术方法
#     def __str__(self):
#         return f"Student类对象,name:{self.name},age:{self.age}"
#     #__lt__魔术方法
#     def __lt__(self, other):
#          return self.age < other.age
#     #__le__魔法
#     def __le__(self, other):
#         return self.age <= other.age
#     #__eq__魔法
#     def __eq__(self, other):
#         return self.age == other.age
#
# stu1 = Student("Jack",22)
# stu2 = Student("Jack",22)
#
# print(stu1)
# print(str(stu1))    #都是打印stu的内存地址
# print(stu1 < stu2)  #True
# print(stu1 > stu2)  #False
# print(stu1 >= stu2) #False
# print(stu1 <= stu2) #True
# print(stu1 == stu2) #True

#演示面向对象封装思想中私有成员的使用
# 定义一个类，内含私有变量和私有成员方法
# class Phone:
#     #以__开头的属性和方法都是私有的
#     __current_voltage = None  #当前手机运行电压
#
#     def __init__(self, voltage):
#         self.__current_voltage = voltage
#
#     def __keep_single_core(self):
#         print("让CPU以单核运行")
#
#     def call_by_fiveG(self):
#         if self.__current_voltage >= 1:
#             print("fiveG属性已经开启")
#         else:
#             self.__keep_single_core()
#             print("电量不足，无法使用5G，并已设置为单核运行进行充电")
#
#
# phone = Phone(5)
# # print(phone.__current_voltage) #无法被直接访问到私有属性
# # phone. __keep_single_core()    #无法被直接访问到私有方法
# phone.call_by_fiveG()

# class Phone:
#     __is__5g_enable = False
#
#     def __check_5g(self):
#         if self.__is__5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭，使用4g网络")
#
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
# phone = Phone()
# phone.call_by_5g()

#继承
# 1.演示单继承
# class Phone:
#     IMEI = None  # 序号
#     producer = "Apple"  # 产商
#
#     def call_by_4g(self):
#         print("4g通话")
#
#
# class Phone2022(Phone):
#     face_id = "10001"
#
#     def call_by_5g(self):
#         print("2022年新功能：5g通话")
#
# phone2 = Phone2022()
# print(phone2.IMEI)
# print(phone2.producer)
# phone2.call_by_4g()
# print(phone2.face_id)
# phone2.call_by_5g()

# 2.演示多继承
# class Phone:
#     IMEI = None  # 序号
#     producer = "Apple"  # 产商
#
#     def call_by_4g(self):
#         print("4g通话")
#
# class NFCReader:
#     nfc_type = "第五代"
#     producer = "HW"
#
#     def read_card(self):
#         print("NFC读卡")
#
#     def write_card(self):
#         print("NFC写卡")
#
# class RemoteControl:
#     rc_type = "红外遥控"
#
#     def control(self):
#         print("红外遥控开启")
#
# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass  #表示跳过
# phone = MyPhone()
# print(phone.IMEI)
# print(phone.producer)
# phone.call_by_4g()
# print(phone.nfc_type)
# print(phone.producer)
# phone.read_card()
# phone.write_card()
# print(phone.rc_type)
# phone.control()

#3.复写
# class Phone:
#     IMEI = None
#     producer = "HW"
#
#     def call_by_5g(self):
#         print("使用5g网络进行通话")
# #定义子类，复写父类成员
# class Myphone(Phone):
#     producer = "Apple"
#
#     def call_by_5g(self):
#         print("开启CPU单核模式,确保通话的时候省电")
#         print("使用5g网络进行通话")
#         #方式一：通过父类名去调用
#         print(f"父类的厂商是：{Phone.producer}")
#         Phone.call_by_5g(self)
#         #方式二：通过子类去调用
#         print(f"父类的厂商是：{super().producer}")
#         super().call_by_5g()
#         print("g关闭CPU单核模式，确保性能")
# phone = Myphone()
# phone.call_by_5g()
# print(phone.producer)

#类型注解
#按住ctrl + p 可查看方法里面的参数类型
#基础数据类型注解
# var_1: int = 10
# var_2: float = 3.1415926
# var_3: bool = True
# var_4: str = "Alan"
# import  json
#类对象类型注解
# class Student:
#     pass
# stu: Student = Student()
# 基础容器类型注解
# my_list: list = [1,2,3]
# my_tuple: tuple = (1,2,3)
# my_set: set = {1,2,3}
# my_dict: dict = {"name":"Alan","age":22}
# my_str: str = "abcdefg"
#容器类型详细注解
# my_list1: list[int] = [1,2,3]
# my_tuple1: tuple[int] = (1,2,3)
# my_set1: set[int] = {1,2,3}
# my_dict1: dict[str,int] = {"height":171,"age":22}
#在注释中进行注解
# 按住alt + enter 会自动导包
# var_1 = random.randint(1,10)           #type: int
# var_2 = json.loads('{"name":"zhangsan"}')  #type: dict[str,str]
# def func():
#     return 10
# var_3 = func()                         #type: int
#类型注解的限制













