# 编辑器：用于编写Python代码的软件 参考Pycharm或VS Code
# 解释器：用于执行编写完成的Python 参考我们安装完成的Python.exe

# 变量：是内存中命名的存储位置，变量的值可以实时动态变化。
# 在Python中，通常同一缩进格式的区域为程序作用域，作用域内的变量叫做局部变量，变量在出作用域后会被释放。
# 写在最顶格外面的即为全局变量。例如在函数体外的变量为全局变量，函数体内的变量为局部变量。

# a  = 1  #  ===> 将 1 定义给 a
# b  = 20  # ===> 将 20 定义给 b
# c,d ='ladies','gentlemen' #  ===>分别定义
# print(f'a是{a}')
# print(f'b是{b}')
# print(f'c是{c}')
# print(f'd是{d}')
# print(f'c,d一起输出{c,d}')

# 变量名称定义后会占用一定的内存空间，如果使用完成后可以选择将其释放。方法是 del (变量名)
# a = 10
# del(a)
# print(a) # 变量a已经被释放，再print会报错

# 变量命名规则：
# 1不得使用作为数字开头；
# 2不得使用空格，可以用下划线连接变量名称；
# 3不得使用标识符号（#）在其中；
# 4不得使用中文作为变量名称；
# 5不得使用以下关键字作为开头
# 简记：2种情况不能做开头：数字、关键字；
#      3种情况不允许出现：空格、标识符（#）、中文

# 注释语句
# Python中 #号右边的内容无需Python解释器理解，通常用于Python中注释语句时使用。
# 可以用于程序测试语句中，注释以后无需删除原句，用于下次使用。
# 多行注释使用三引号进行注释：""" 注释内容 """
# 例如：
# print('准备运行一个注释语句')  #注释。。。
# print("注释语句")
#  多行注释可以使用三引号进行注释。

# 缩进
# 缩进语句通常用在特殊语句的特殊写法，可以确定语句的执行区域。
# a = 10
# if a ==10:
#     print('执行if !')
#     print('if语句执行完成！')
#     if a=>10:
#         print()

# 输出语句print()
# 输出语句print()是Python中最常见的语句，该语法会将内容完整的输出到电脑控制台上或文件当中。
# a =10
# print(a)  # 输出变量
# print(3)  # 直接输出数字
# print('Hello')  # 添加引号可以直接输出文本
# print("Hello" +" World") #输出字符串 Hello World 字符串拼接
# print(1+2)  #  直接输出算数结果
# print()  # 直接输入print()会换行

# 多行输出
# print()语句只能输出单行，如果要输出多行可以用到三引号或转义字符（本处讲三引号）  、
# 三引号：3 个单引号或3个双引号
# print会从你引号的地方一直输出到最后一个引号位置，可以换行。
# print('''Alan is the best man in the world''')

# 选择性输出
# 如果一句完整的话不需要完整输出，那么可以用到切片操作，本处将会简单介绍切片操作，后续会详解切片操作
#例如：
# word = 'ABCDE'
#如果只需要输出ABC，而不要DE  切法 ：[ ：终点]
# print(word[:3])
# 如果不需要输出ABC   切法： [起点：]
# print(word[3:])

# 常见的基础数据类型
# 整数值类型- int -98；
# 浮点数类型- float -3.1415926；
# 布尔值类型- bool -True，False；
# 字符串类型-  str -‘Hello Alan’,‘你好’。
# int_ = 98
# float_ =3.1415
# bool1 = True
# bool2 = False
# str_ = 'Hello everyone'
# print(f'int_是{int_}，数据类型是 {type(int_)}\n')        #  通常的，直接写出的整数是int整数类型。
# print(f'float_是{float_}，数据类型是 {type(float_)}\n')  #  通常的，直接写出的小数是fLoat浮点数类型。
# print(f'bool1是{bool1}，数据类型是 {type(bool1)}\n')     #  通常的，直接写出的True是布尔值类型。
# print(f'bool2是{bool2}，数据类型是 {type(bool2)}\n')     #  通常的，直接写出的False是布尔值类型。
# print(f'str_是{str_}，数据类型是 {type(str_)}')          #  通常的，直接写出带引号的文本是字符串类型。

# 数据类型转换
# 在平时编写代码的过程中，会常常出现不同的数据类型， 而不同的数据类型是无法进行连接使用或比较的。
# 所以这个时候就需要用到了 “数据类型转换”。
# Python中，可以使用type(变量名)查看该变量的数据类型。
# 数据类型转换：只需要将想转化的数据类型写出来，并在括号内写入变量名称即可
# new_int_float = float(int_)
# new_float_int = int(float_)
# new_bool1_int = int(bool1)
# new_bool2_int = int(bool2)
# new_int_str = str(int_)
# print(f'int_是{int_}，新的int_到float的值是{new_int_float}，数据类型是{type(new_int_float)}\n')
# print(f'float_是{float_}，新的float_到int的值是{new_float_int}，数据类型是{type(new_float_int)}\n')
# print(f'bool1是{bool1}，新的bool1到int的值是{new_bool1_int}，数据类型是{type(new_bool1_int)}\n')
# print(f'bool2是{bool2}，新的bool2到int的值是{new_bool2_int}，数据类型是{type(new_bool2_int)}\n')
# print(f'int_是{int_}，新的int_到str的值是{new_int_str}，数据类型是{type(new_int_str)}\n')

# 连接输出
# 如果要打印输出多个同类型变量值，可以使用“+”将其连接，或是使用逗号‘,’分割开。
# 区别：“+”无空格，逗号“，”有空格。
# 文本添加会直接连在一起  例：
# a ='A'
# b ='B'
# print(a+b) #字符串拼接
# c = 'Alan'
# d = '20'
# e = 20
# print('我叫'+ c + '，今年',d,'岁了，请多多光照！')
#print('我叫'+ c + '，今年'+e+'岁了，请多多光照！') #TypeError: can only concatenate str (not "int") to str
# 要同时输出打印时，需要相同的数据类型才能同时输出，否则会报错。
# print('我叫'+ c + '，今年'+str(e)+'岁了，请多多光照！')

# 格式化字符串
# 使用格式化字符串可以无需通过转化类型就可以直接输出，同时格式化字符串还可以输出表达式。
# 第一种：%占位符：用 %号占位，其中%s占字符串，%d占整数型，%f占浮点数，%b占布尔值；依次填入且不能调整位置
#  %例：
# name = 'Alan'
# age = 20
# print('我叫%s,%d岁'%(name,age))
# 第二种：.format()占位：用.format语句进行变量存储，用{}占位，依次填入，但可以调整位置
# .format例：
# name = 'Alan'
# age = 20
# print('我叫{0}，今年{1}岁了。'.format(name,age))
# 第三种：f-string格式占位：在引号左侧写一个f，文本内容添加{}即可对应提取变量依次填入。
# f-string例：
# name = 'Alan'
# age = 20
# print(f'我叫{name},今年{age}岁了')

# 格式化高级使用：
# 在平时编程当中，为了编写规范，通常会用到隔一段距离输出或是精确小数点。这时候可以用到格式化的高级使用进行代码优化。
# 空格使用：空出内容对应长度 n。其中包括字符串长度 d，前面空出n-d个长。
#  % 类型
# name ='Alan'
# age =10
# print('%10s'%name)
# print('%10d'%age)
#  小结：%长度 类型，表示空格 ，严格遵守类型符号 s 文本 d整数 f小数 b布尔
#  .format 类型
# name = 'Alan'
# age = 20
# print('{0:10}'.format(age))            #  ===> 数字类型可以直接写 起点 ：终点长度
# print('{:>10}'.format(name))           #  ===> 字符类型需加上方向符号 <>
# print('{:>10}{:<10}'.format(name,age)) #  > 是向右对齐，即向右边空出位置，< 同理为向左
#  小结：加上 冒号（：），表示空格；
#  其中数字类型可以直接写 起点 ：终点长度 ，起点默认为0 ；   文本需加上方向符号
#  方向符号方法  数字类型可以和文本共用
# f-string类型没有空格功能

# 小数点使用：
# % 类型
# pai =3.1415926
# print('%f'%pai)  #  ===>%f表示浮点数，自动精确到最后一位小数，四舍五入
# print('%.3f'%pai)  #  ===>加上  .3f 即精确三位小数
#  小结：%f 默认精确到最后一位数，加上 .位数f   可以精确到对应小数点位置，整数默认补0
# .format类型
# pai =3.1415926
# print('{:.3f}'.format(pai))  #  ===> 精确小数点3位
# print('{:.3}'.format(pai))  #  ===>有效长度 3位
# print('{0:.5f}'.format(pai))  # ===> 有效长度五位，精确5位小数
# print('======')
# print(pai)
#  小结：默认起点为0，: . 字符有效长度。加上f > :.位数f  可以精确到对应小数点位置，整数默认补0
# f-string类型没有精确小数功能

# 空格和精确小数同时使用
# % 类型
# pai = 3.1415926
# print('%10.3f'%pai)  #===>  %10.3f，一共总宽度为10，小数点精确后3位
#  小结 ：%长度 .精确位数
#  .format 类型
# print('{0:10.3f}'.format(pai))  # ===> 0:10.3f ，一共总宽度为10，小数点精确后3位
# 小结： {起点：终点 .精确位数}
# 小结：%号 语句规范无法调整位置，.format语句较规范且功能强大，f-string方式简洁且主要以输出内容为主

# 计算机进制
# 十进制：Python默认进制。缩写：DEC。如：整数：0、-1、9、123；
# 二进制：以0b开头，缩写：BIN。如：0b101、0b100；
# 八进制：以0o开头，缩写：OCT。如：0o35、0o11;
# 十六进制：以0x开头，缩写：HEX。如：0x10、0xfa、0xabcdef;

# 进制转换
# Python中默认机制为 十进制。进制也算前面的数据类型一种。
# 在平时编写代码或其他数据加密过程当中，通常需要进制转换进行数据加密解密等，这时就需要了进制转换。
# 既然也算数据类型一种，那么它转化方法跟数据类型转化同理。
# number = 123
# bin_ = bin(number)
# oct_ = oct(number)
# hex_ = hex(number)
# print(f'''初始值（十进制）：{number};
# 转化后二进制是：{bin_};
# 转化后八进制是：{oct_};
# 转化后十六进制是：{hex_}.''')

# 转义字符
# 通常需要文本空格或换行时，可以直接使用转义字符进行便捷操作
# 换行：\n（newline）：将一段长文本另起一行继续表示。
# print('new\nline')
# 回车：\r（return）：将同一段字符串内的转义符前面的内容清除取代
# print('re\rturn')
# 水平制表符：\t（tab）：自动填充4个单位的空格。
# print('ta\tb')
# print('hello')
# 退格：\b（backspace）：在一个字符串内退去一个字符。
# 原字符：在引号前加r或R：让本字符串内的转义字符不起作用。
# print(r'un\nknow')

# input()输入语句
# 在编写过程中，通常会遇到需要与用户交互进行输入内容，这时候就可以使用input()语句进行输入内容
# 使用时只需要写出input()即可，如果需要接收input()传来的内容，可以定义一个变量将input内容赋予给该变量
# use_input = input()# 括号内可以添加文本用来提示输入
# print(f'use_input是{use_input}')
# 如果可以接收内容以后，我们是否可以通过内容输入制作一个简单的计算器呢？
# num1 =int(input('请输入一个数字：'))
# num2 =int(input('请输入一个数字：'))
# print(num1+num2)
# print(f'num1类型是：{type(num1)}')
# input()入口接收函数默认 字符串（str）类型。可以根据实际使用时更改数据类型

# input() 语句高级使用：.split()
# 通常在接收用户所需要输入的内容时，经常会用到分割字符传达过来的字符
# 例如，题目要求：num即将接收六个内容，用空格分开：1 2 3 4 5 6；
# 那么可以用到字符的分割写法：.split()

#例如：
# num = input().split()
# print(num)
# 写多少个就接收多少个，遇到需要分割的内容依次作为一个单位分割
# #  可以声明多个变量，会依次填入对应变量
# a,b = input().split()
# print(a)
# print(b)
# 这里就不是输多少接多少，只会接收变量数个内容，超过或缺少 都会报错。
# 批量修改.split()内容数据类型
# num = list(map(int, input().split()))
# print(num)
# 变量名 = list(map(基本数据类型，*iterables))
#这个是随便接受任何数据长度的内容，以空格为结尾，并默认转成int类型，转换失败会报错。结果会存储到列表当中(列表详解在后文)
# 原生字符串也使用.split()写法
# word = 'Hello everyone! I am Alan'.split()
# print(word)
# .split()写法默认会从头切到尾，如果要限制切割数量，可以用下面的写法
# word = 'I am Alan ,  I am 20 years old ,Thank you！'.split()
# print(word)

# *eval()函数
# eval是Python的一个内置函数，功能十分强大，这个函数的作用是：可以 将字符串当成有效的表达式 来求值 并 返回计算结果。
# a = input()
# a = eval(a)
# print(a,type(a))
# eval() 直接实现字符串转化至整数型，并且计算
# s = '1+2+3*4-5'
# print(eval(s))
# 同样可以结合input()进行使用
# num = input()
# print(eval(num))
# num1 = eval(input())
# print(num1)
# 8+7
# 15
# 7+8
# 15
# eval() 直接实现带变量计算
# a  = 1
# print(eval('a+2'))
# eval()函数的缺点：eval函数还有一项功能，就是可以直接执行命令。这也同时也是它的一项缺点
# eval('print("Hello Everyone!")')  #Hello Everyone!
# 在后续如果需要做大项目的编程时，尽量避免使用eval作为与用户的交互处，避免出现恶意输入。

#运算符优先级：算术优先级 > 位运算符 > 比较运算符 > 布尔运算符 > 赋值运算符（可以通过括号()改变优先级）

#算术运算符
# ＋ - * / // % **
# /算符	描述	实例
# +	加 - 两个对象相加	a + b 输出结果 30
# -	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
# *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
# /	除 - x除以y	b / a 输出结果 2
# %	取模 - 返回除法的余数	b % a 输出结果 0
# **	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
# //	取整除 - 返回商的整数部分（向下取整）	>>> 9//2 4 >>> -9//2 -5
# a = 2
# b = 3 #或a,b = 2,3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)

# 位运算符
# <<  >> （&、|、^、~ 这四个了解即可，主要了解外面两个）
# 下表中变量 a 为 60，b 为 13，二进制格式如下：
# a = 0011 1100
# b = 0000 1101
# -----------------
# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a  = 1100 0011
# 位算符	描述	实例
# <<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
# &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
# |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
# ^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
# ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。

# 比较运算符
# <   <=  >  >=  !=
# 以下假设变量a为10，变量b为20：
# 运算符	描述	实例
# ==	等于 - 比较对象是否相等	(a == b) 返回 False。
# !=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
# <>	不等于 - 比较两个对象是否不相等。python3 已废弃。	(a <> b) 返回 true。这个运算符类似 != 。
# >	大于 - 返回x是否大于y	(a > b) 返回 False。
# <	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。	(a < b) 返回 true。
# >=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
# <=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 true。

# 布尔(逻辑)运算符
# and or not in (not in)
# Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
# 运算符	逻辑表达式	描述	实例
# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

# 赋值运算符
# ==   += -= *= /= //= %=
# 以下假设变量a为10，变量b为20：
# 运算符	描述	实例
# =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
# +=	加法赋值运算符	c += a 等效于 c = c + a
# -=	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a

# 判断语句:if
# 判断条件语句是否成立，成立则执行区域内代码
# a = 5
# if a==5:
#     print('a=5')
# print('Done!')
# 判断语句的嵌套：if-elif-else
# 判断语句支持多项成立条件，执行不同情况语句，且允许嵌套
# a = 10
# if a>5:
#     if a>8:
#         if a>=10:
#             print(a)
# a= int(input())
# if a <20:
#     if a <5:
#         print('该数在1-5之间')
#     elif a<10:
#         print('该数在5-10之间')
#     elif a<15:
#         print('该数在10-15之间')
#     else:
#         print('该数在15-20之间')
# else:
#     print('你输入的数字不正确')

# range()生成数 语句
# range(起点：终点（但不包含终点）：步长（默认为1）)
# for循环语句是用于将一个可迭代对象逐个进行循环输出的方法函数，主要写法就是
# for var in iter :

# iter为一个可迭代对象，可迭
# 代对象主要为range函数，字符串、数组等等。在Python里面来说，几乎所有的内容都属于可迭代对象；
# iter为一个可迭代对象，可迭代对象主要为range函数，字符串、数组等等。在Python里面来说，几乎所有的内容都属于可迭代对象；
# var为一个赋值变量，正如上面所说，for循环是将一个可迭代对象逐个赋予给一个新变量以此达到赋值循环的目的。
#在Python中，for循环的思想就是：将一个可遍历（迭代）的项目，对其内容每一个元素依次作为循环变量并使用。
# 同时，Python还支持循环结束后的预处理，当你需要在程序正常运行结束时执行某一语句时，
# 你可以使用else语句(详见for循环的特殊写法)。
# for循环语法结构：
# for 循环变量 in 循环对象: # 循环主体
#     循环执行语句......
# else: # 当循环结束后执行某一语段，那么你需要写上else语句
#     else语段 # else语段里，不允许使用循环变量。
# 实例1: 循环字符串
# 循环字符串，此时Python会将字符串内所有内容逐个赋予给循环变量word，并允许你在for的缩进作用域内使用循环变量word。
# for word in "Python":
#     print("当前字母: {}".format(word))
"""
实例1 输出结果：
当前字母: P
当前字母: y
当前字母: t
当前字母: h
当前字母: o
当前字母: n
"""

# 实例2：循环列表序列
# 在Python中，你可以在特定的方法中循环使用你的临时存储数据方法，包括你的列表。

# color_lst = ["red", "black", "blue"]
# for color in color_lst:
#     print("当前颜色: {}".format(color))
'''
实例2 输出结果：
当前颜色: red
当前颜色: black
当前颜色: blue
'''

# 实例3：计数循环
# Python提供了range()函数结合for循环能将你的代码段运行多次。
# range()函数同时还是一个生成数函数，它的函数参数为range(start, end, step=1)。
# 其中，参数含义分别为：start=开始计数的位置，end=不包括自身的结束位置，step=每次的步长。
# for i in range(3):
#     print("当前循环数：{}".format(i))
"""
实例3 输出结果：
当前循环数：0
当前循环数：1
当前循环数：2
"""
# for循环的特殊写法
# 在for循环当中，有一个特殊的分支写法：即for...else:写法
# 该写法的主要用于：当程序正常循环结束以后，执行else语句的内容；
# 小Tips：如果程序异常退出或使用了break语句，则不会执行else
# for i in range(0,3,1):
#     print(i)
# else:
#     print('done!')
# output: 0 1 2 done!
# 非正常结束循环：程序异常退出、使用了break语句，不会执行else
# for i in range(3):
#     if i:
#         break
# else:
#     print("Done!")
# # >>> 没有输出
# target = 3
# for i in range(3):
#     for j in range(4):
#         if i + j == target:
#             print(i,j)
#             break
# else:
#     print('done')

# while 循环语句
# while循环形如其他编程语言，只要条件成立，则while循环继续；
# 在Python的while循环当中，循环规则为先判断条件后循环；循环执行语句可以是单个语句或语句块。
# 判断条件可以是任何表达式，任何非零、或非空（null）的值均为 True。当判断条件假 False 时，循环结束。
# while循环语法结构：
# while 判断条件(condition)：
#     循环执行语句......
# else: # 当循环结束后执行某一语段，那么你需要写上else语句
#     else语段

# # 实例1：计数循环
# count = 0
# while (count < 5):
#    print("当前循环数:".format(count))
#    count = count + 1
# """
# 实例1 执行结果：
# 当前循环数: 0
# 当前循环数: 1
# 当前循环数: 2
# 当前循环数: 3
# 当前循环数: 4
# 当前循环数: 5
# """
#
# # 实例2：循环使用 else 语句
# # 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
# while (count < 5):
#     print("The count is:".format(count))
#     count = count + 1
# else:
#     print("循环结束！！！")
# """
# 实例2 执行结果：
# 当前循环数: 0
# 当前循环数: 1
# 当前循环数: 2
# 当前循环数: 3
# 当前循环数: 4
# 当前循环数: 5
# 循环结束！！！
# """

# # 实例3：无限循环
# # 结合while循环的使用细则，当条件成立 True时，那么循环就会一直进行下去。利用这个机制，我们可以写出无限循环格式。
# while True:
#     print("RUNNING!")
#
# """
# 实例3 执行结果：
# RUNNING!
# RUNNING!
# RUNNING!
# RUNNING!
# RUNNING!
# ...... (此时无干预的情况下程序将一直输出下去)
# """
# # 无限循环下，你可以使用CTRL+C 中断循环

#切片操作
# 切片操作可以用在我们Python代码中许多地方，其主要功能就是可以提取指定位置或区域的内容
# 在Python中，表示位置的区域大多数都是会从0开始计数，所以长度为n的单位，在Python中的长度就是n-1
# 切片常用表示和其具体含义：变量名称[a : b : c]，其中并不是每一个内容都是必须填入的。
# c = 间隔位置/方向（c默认=1，c为正数时，从左往右；c为负数时，从右往左）c的值非常重要！！因为它关系着a b的方向
# a = 开始位置（包括该点，默认为开头，c为正数时从开头位置开始，c为负数从结尾开始）；
# b = 结束位置（不包括该点，，c为正数时到结尾位置结束，c为负数时到开头位置结束）；
# a和b确定的起点和终点，确立起切片的执行区域的方向
# c 确定的间隔/方向，确立起切片的开始方向。
# 这么说你可能会懵圈，简单来说，a与b会确定起一个切片的作用区间，例如从最右边到最左边
# a和b的方向需要与c的方向相同，才可以取出内容。
# 如果a和b的方向和c的方向不同，切片会切不出内容。
# 如果ab不填，就默认为c的方向作为起点终点
# 查看切片的步骤
# ①  先通过起点和终点，判断其执行区域的方向
# ②  再看c的正负，判断其开始方向
# 切片内容翻转
# word = "Python"
# result = word[::-1]
# print(result)  #nohtyP

# 切片1：[开始位置：]
# # 【开始（不包括）:】
# word = "Python"
# result = word[1:]
# print(result) #ython

# 切片2：[ :结束位置]
# #  【开始位置（不包括）：结束位置（不包括）】
# word = "Python"
# result = word[:4]
# print(result) #Pyth

#切片3：[开始：结束：间隔]
#  间隔n-1个位置进行取出
# word = "1234567"
# result = word[1:6:2]
# print(result)
# word = "1234567"
# result = word[6:1:-1]   #开始和结束的方向要与c的方向相同
# print(result)

# 列表：list()
# 列表(list)是一种有序的容器，放入list中的元素将会按照0~n的顺序排列。
# 形如：带着中括号的 [ ]可以看作是列表
# L = ['Alice', 66, 'Bob', True, 'False', 100]
# print(L)
# 列表内的数据以每一个“，”逗号作为间隔，一个间隔一个数据。采用0~n-1的方式排序。
# 列表内的元素可以存放任意数据类型的内容，且放进的内容数据类型不会改变。也是Python当中常用的数据存储方式。
# 列表定义方法：

#1.符号定义法：
# L = [] 或 L = list()
# print(type(L))
# data_list = [1,2,6,8,"Hello","Jupyter0","teach"]
# print(type(data_list))
# print(data_list)
# 直接定义list的方法非常简单，使用中括号[ ]把需要放在容器里面的元素括起来，就定义了一个列表。
# <class 'list'>
# <class 'list'>
# [1, 2, 6, 8, 'Hello', 'Jupyter0', 'teach']

# 2.名称定义法：
# data = "123998"
# data_list = list(data)
# print(data_list)
# 定义list的方法是声明一个变量，写出其函数名称即可:变量名称 = list()
# 这种方法会逐个将内容拆分，逐个放进列表当中，类似于for循环
# ['1', '2', '3', '9', '9', '8']
# 直接定义list的方法非常简单，使用中括号[ ]把需要放在容器里面的元素括起来，就定义了一个列表.

# 列表常见操作
# 1.查看列表长度
# 通常在一段长列表当中，我们一个个数列表的长度太难，所以我们可以用len()方法获取列表长度。
# 获取列表长度：len(列表名称)，这里就是直接从1~n写出它的长度，不会从0开始算
# L = ['Alice', 66, 'Bob', True, 'False', 100]
# ER  = [[1,2,3],
#       [2,3,4]]
# print(len(L))
# print(ER[0][1])
# 2.获取列表内容
# 获取列表内容，可以通过列表位置获取列表内容。
# 方法：列表名称【提取的位置】0~n
# L = ['Alice', 66, 'Bob', True, 'False', 100]
# print(L[3])
# True
# 如何逐个遍历列表内容呢？
# L = ['Alice', 66, 'Bob', True, 'False', 100]
# for i in range(len(L)):
#     print(L[i])
# 3.增加内容进入列表当中
# 当已定义好一个列表，那么我们需要不断添加内容数据。
# 1.直接添加法，将内容添加到列表最末尾：列表名称.append(填入的内容)。
# #添加在最末尾：列表名称.append(填入的内容)
# L = ['Alan',22,'Konglingjun',True,34.6,'False']
# L.append('None')
# print(L)
#2.位置添加法：将内容添加到列表的指定位置：列表名称.insert(插入位置，"填入的内容")
# L1 = ['Alan',22,'Konglingjun',True,34.6,'False']
# L1.insert(2,'None')
# print(L1)
#3.列表拼接法：L1.extend(L2) 将列表L2拼接到列表L1后面
# L1 = ['My','name','is','Alan']
# L2 = ['I' ,'am','22','years','old']
# L1.extend(L2)
# print(L1)
#小结：填入的位置序号，就是它即将放置的位置。

# 4.删除列表内容
# 1.直接删除法：列表名称.clear().
# L1 = ['Alan',22,'Konglingjun',True,34.6,'False']
# L1.clear()
# print(L1)
# 2.位置删除法：可以用.pop方法删除：列表名称.pop()。
# 其中pop()括号内容可不填内容，默认删除最后一个元素，填入数字删除指定位置
# L1 = ['Alan',22,'Konglingjun',True,34.6,'False']
# L1.pop()
# L1.pop(1)
# print(L1)
#3内容值删除法：列表名称.remove().
# L1 = ['Alan',22,'konglingjun',True,34.6,'False']
# L1.remove('konglingjun')
# print(L1)

#5.重新组织列表
# 1.reverse:把列表中的数据元素头尾反转重新排列。用法:列表名称.reverse().
# L1 = ['Alan',22,'Konglingjun',True,34.6,'False']
# L1.reverse()
# print(L1)
#2.sort:把列表中的数据元素按照大小顺序重新排列 用法:列表名称.sort().
# L1 = [1,2,7,9,3,6,9,2,7]
# L1.sort()
# print(L1)
# L1.sort(reverse=True)
# print(L1)
# 3.reversed/sorted 操作
# 得到重新排列的列表，不会影响原来的列表
# L1 = [1,2,7,9,3,6,9,2,7]
# L2 = L1.__reversed__()
# print(L1)

# 6.替换列表内容
# 讲了取增删的方法，那么如何修改列表里面的内容呢？
# 方法：列表名称【替换的位置】 = 替换名称
# 注意：这种方法不能作为添加内容的方法，因为替换位置超出列表长度会报错
# L1 = ['Alan',22,'Konglingjun',True,34.6,'False']
# print(L1[0])
# L1[0] = 'King'
# print(L1[0])

# 统计内容出现次数和位置
# 列表中，可以使用.count()方法统计字符出现同类型的个数
# 列表中，可以使用.index()方法输出该字符第一次出现在列表的下表位置（0~n）
# L = ['Alice', 66, 'Bob', True, 'False', 100, 100, "100"]
# print(L.count(100))  # 2
# print(L.index(100))  # 5
# 到此为止，列表的基础常见操作讲完了，内容覆盖了如何定义列表，如何取、增、删、改等操作

# 字典：dict()
# Python的dict就是专门保存映射的容器，例如可以使用dict可以方便的保存“名字”->“成绩”的映射。只要取出名字，就能知道其对应成绩
# 解决上面的问题中，我们可以使用名字作为key，成绩作为value。
# 在dict中，每一项包含一个key和一个value，key和value是一一对应的

# 定义字典
# 1.符号定义法
# 在定义里，我们使用花括号{}表示这是一个dict
# 然后key和value之间使用冒号:分割，并且每一组"key:value"的最后，以逗号","表示这一组的结束
#  形如
# d = {
#         'Alice': 45,
#         'Bob': 60,
#         'Candy': 75,
#         'David': 86,
#         'Ellena': 49,
#         'Gaven': 86,
#     }
# print(type(d))
# print(d)
# 2.直接定义法
# 同列表方法
# d = dict()
# print(d)

# 字典常见操作
# 1.查看长度
# d = {
#         'Alice': 45,
#         'Bob': 60,
#         'Candy': 75,
#         'David': 86,
#         'Ellena': 49,
#         'Gaven': 86,
#     }
# print(len(d))
# 2.获取字典内容
# 获取字典里的所有key可以使用字典名称.keys()获取，括号内不可以填入内容，会默认输出从上至下所有的key
# d = {
#         'Alice': 45,
#         'Bob': 60,
#         'Candy': 75,
#         'David': 86,
#         'Ellena': 49,
#         'Gaven': 86,
#     }
# print(d.keys())
# 2.1获取字典里的value
# dict中，可以提供通过key找到对应value的功能，例如通过d[key]的形式，就可以得到对应的value。
# d = {
#     'Alice': 65,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 89,
#     'Gaven': 86
# }
# print(d['Bob'])
# print(d['Alice'])
# 2.2获取所有的values()
# d = {
#     'Alice': 65,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 89,
#     'Gaven': 86
# }
# print(d.values())
# 小Tips
# 2.3这里也可以结合for循环使用items()方法遍历字典，分别提取到出所有的key和value
# d = {
#     'Alice': [65,75],
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 89,
#     'Gaven': 86
# }
# print(d.items())
# for key,value in d.items():
#     print("{} ==>{}".format(key,value))
# 3.添加/更改 字典内的数据
# 添加/更改的方法：字典名称【填入/更改的key】 = 【填入/更改的value】
# 要点：
# 当key不存在时，往dict中添加对应的key: value元素。
# 当key存在时，会更新dict，用新的value替换原来的value。
# d = {
#     'Alice': [65,75],
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 89,
#     'Gaven': 86
# }
# d["Candy"] = [45,67]
# print(d)
# 4.删除字典里的内容
# 字典中，可以使用.pop()
# 方法删除对应key的内容。
#  方法：字典名称.pop("Key的名称")
# d = {
#     'Alice': 65,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 89,
#     'Gaven': 86
# }
# d.pop("Alice")  # 会返回删除掉的key的value值
# print(d)
# {'Bob': 60, 'Candy': 75, 'David': 86, 'Ellena': 89, 'Gaven': 86}
#  清空字典
# d = {
#     'Alice': 65,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 89,
#     'Gaven': 86
# }
# d.clear()
# print(d)

# 元组：tuple()
# 元组(tuple)
# 和list一样，也是一个有序容器，定义元组的方式是使用小括号()
# 将元组内的元素括起来。
# 特点：tuple容器与List容器的差别就在于，tuple容器中的数据不可更改，不可添加，
# 所以在实际编程中，tuple经常用于存放固定不变的数据。
# 定义元组的方法:
# 1.符号定义法:
# 可以使用小括号()直接声明一个元组。
# 2.直接定义法
# T = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(type(T))
# print(T)
# class <'tuple'>
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 3.变量定义法
# T = 1, 2, 3, 4, 5, 6
# print(T)
# 访问元组数据出现次数以及下标识
# 同列表的方法一样，用count()
# 统计同类型数据出现个数，用.index()
# 方法统计数据第一次出现的个数

# 修改 / 替换 / 删除元组内的数据
#  能不能做呢？
# T = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 因为元组内的数据不允许被操作，所以元组不支持修改/替换/删除的操作

# 集合：set()
# set集合内的数据没有顺序(无法提取)，且不允许重复，如果存在重复的数据则会覆盖，打印输出时只会输出一个数据。
# set集合通常使用一个小括号表示([])，内部数据常用列表保存
# 1.定义集合的方法
# 直接定义法
# 因为集合和元组同样使用小括号()进行表示，所以在具体使用过程当中，小括号()会默认定义为元组，set只有如下方法
# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# s = set(names)
# print(s)
# se = set()
# print(se)

# 2.集合常用操作
# 集合当中，数据填入以后集合会默认进行内容排序，数字从到大小
# s = set([1, 4, 3, 2, 5])
# print(s)

# 3.读取集合内容
# 因为集合是没有顺序的，所以无法直接读取集合中指定位置的内容。但是可以判断元素是否在集合当中
# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# name_set = set(names)
# print('Alice' in name_set)

# 4.添加set内的数据
# 1.通过定义变量，并配上“.add”可以直接添加单一的数据进入。
# 在集合set中，如果内容已存在，则不会添加
# 方法：集合名称.add(添加的内容)
# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# name_set = set(names)
# name_set.add('Bob')
# print(name_set)
#2.批量添加内容，可以用集合.update方法添加多个内容
# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# new_names = ['Hally', 'Isen', 'Jenny', 'Karl']
# name_set = set(names)
# name_set.update(new_names)
# print(name_set)

# 5.删除set集合内的数据
# 1.set中提供了“remove()”的方式删除数据。
# 但如果数据不在set中，系统则会报错。
# name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy'])
# name_set.remove('enny')
# print(name_set)
# # 如果不知道内容是否在set当中，避免报错，可以使用if语句进行判断内容是否在set当中进行下一步执行
# name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy'])
# if 'enny' in name_set:
#     name_set.remove('enny')
# else:
#     print("该元素不存在于集合中")
# print(name_set)
# 2.set中remove()方法不存在会报错，但也同时提供了discard()方法不存在时不报错
#  Remove an element from a set if it is a member.
#  If the element is not a member, do nothing.
# name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy'])
# name_set.discard('Jenny')
# print(name_set)

#6.清空set内的内容，同样可以使用clear()方法清空
# name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy'])
# name_set.clear()
# print(name_set)

# 函数
# 1.函数是执行特定功能的一段代码，函数可以将一段功能代码封装起来成为一个新的定义，在需要使用到函数功能时调用即可使用函数内的功能。
# 举例:常用的print()输出函数，查看类型的type()函数，进制转化的的bin()、oct()函数，查看内存位置的id()函数等都是函数，这些函数也叫做内置函数。

# 2.用函数做什么？
# 通常我们在编写代码过程当中，代码会从上至下执行到最后一行。
# 如果我们想要一个功能重复使用，或让其在自己预想的特定时候执行、集成使用特定功能，这个时候我们就可以用到函数的功能。
# 同时，统一封装功能编写函数便于我们对程序的调试维护、提高我们代码的可读性
# 在编写软件代码过程当中，最常用、最简单的编程方式就是函数式编程，程序由函数构成。
# 使用特定功能时均声明好功能函数，这样编程就可以如同搭积木一样的方法了。
# 3.函数的声明
# 1.通常的，编写函数使用定义法：def
"""  函数定义方法：其中中括号处可填可不填
def 任意的函数名称 （a,b）:   
    函数功能体
    [return xxx]  
    函数运行到函数体最后一行，或是return处结束运行，
    return语句的功能主要是将函数运行结果反馈至调用处。
变量 = 函数名称（a,b）
print()
"""
# 2.无需传入参数的函数
# 无需的传入的函数，就是在函数定义与使用的过程当中，不需要往函数内传入内容的函数叫做无参函数。
# def example():
#     print("Alan is so handsome")
#     return
# # return可以返回数字、文字或是表达式。
# example()
# #  传回表达式
# def calc():
#     a = 10
#     b = 20
#     return a+b
# function = calc()
# print(function)
# 3.需要传入参数的函数
# 函数通常在无参数传入时，会固定执行函数体内的所有代码。
# 如果我们需要函数在特定的时候接收来自外部的内容来执行不一样的结果时，
# 我们可以使用需要传参的函数，保持函数的动态性。
# 4.未定义参数的函数
# #  例如：
# def calc(a,b):  # a b统称形式参数 == 形参
#     return a+b
# function = calc(10,20)   # 传入参数位置对应着函数需要的参数位置，10传给a，20传给b。10和20统称为实际参数 == 实参
# print(function)
# 函数中，需要n个参数就必须要传入n个参数，传多或传少均会报错
# 5.已定义参数的函数
# 例如
# def calc(a,b=20,c):# 默认定义好一个参数的值，则可以无需传入指定数量的参数，但必须放置在最右边
# def calc(a,c,b=20):
#     return a+b
# function = calc(10,30)
# print(function)
# 6.可变长度的参数函数
# 1.元组存储的可变参数函数
# 当我们在不确定函数传入的数量，或需要传入较多个内容时，可以使用可变长度的参数函数
# 例如：
# def example(*num):
#     return num
# function = example(1,2,3,4,5,6,7)
# print(function)
# 2.字典存储的可变参数函数
# 可变长度的参数不仅仅是可以存在元组当中，还可以存入到字典；
# 字典存储的可变长度函数，需要特别表明key和value的值，对应着 key = value;
# 例如：
# def example(**num):
#     return num
# function = example(a=1,b=2,c=3,d=4)
# print(function)

# 1.lambda表达式
# lambda表达式是一行的函数。它们在其他语言中也被称为匿名函数。
# 如果你不想在程序中对一个函数使用两次，你可以想到用lambda表达式匿名函数，这样可以使得你的代码变得更加简洁。
# lambda 表达式声明方法：
# lambda用于简单的数据处理
# 表达式名称 = lambda 【即将填入的变量名称】：需要使用变量执行的命令。
# 可以用lambda表达式执行简单的内容处理
# 例如：
# f = lambda x,y : x+y
# # # 调用方法：同函数调用
# print(f(10,20))
# # 调用方法：直接调用
# #  (lambda 【即将填入的变量名称】：需要使用变量执行的命令)(传入的内容)
# print((lambda x,y : x+y)(10,20))

# lambda可用于调用多个函数
# 当我们写好众多函数时，如果需要逐个调用函数相当于要多写许多内容。那么我们可以使用lambda表达式同时调用多个内容
# 例如:
# def t():
#     print("Hello", end="")
# def y():
#     print(" World", end="")
# def p():
#     print(" Python", end="")
# #  (lambda ：【需要调用的函数名称】）())
# (lambda: [t(), y(), p()])()

# 2.程序运行略过：pass语句
# 通常我们在写程序时，初期为了程序后续制作经常会运行调试，但不是每次都能把每一段过程都写完。所以我们可以用上pass语句，让程序跳过该步骤。
# 使用pass语句可以让程序直接跳过该步骤而无需理解,并且不会报错。
# 例如：
# a = 10
# if a < 5:
#     print("a<5")
# else:
#     pass
# for i in range(10):
#     pass
# def example():
#     pass
# example()

#异常处理 try...except......else......finally
#通常我们在写程序时，难免会有部分代码导致程序崩溃。
#那么接下来的写法将讲述如何处理崩溃信息，并且避免程序崩溃。
# 1.try...except语句
# 处理try...except语句时，解释器会先运行try语句中的一句。
# 如果try语句中的程序报错，那么程序就会运行expect语句
# try:
#     for i in xx:
#         pass
# except:
#     print("exit code 1")
#2.也可以对错误类型进行举例，为该类型错误则运行except语句，
#其余的软件可报错。用这种方法可以避免except语句过于广泛。
#具体报错类型可以详见官方开发文档。通用报错名称名为：Exception
# 3.except语句可以拥有多个，但最广泛的except需要放在最后一个。
# try:
#     a = b
#     print(a)
# except SyntaxError:
#     print("SyntaxERROR")
# except NameError:
#     print("NameERROR")
#4. except语句可以把报错描述输出
# try:
#     a = b
#     print(a)
# except Exception as e:  # 把报错命名为e
#     print(f"Erro : {e}")
#5.把except报错类型输出，这里有用到Python内置函数 repr()
# repr()：会返回一个对象的 string 格式。
# try:
#     a = b
#     print(a)
# except Exception as e:
#     print(repr(e)) # 给出完整描述
#     print(repr(e).split('(')[0])  # 使用split提取把报错类型提取出来
#6. try...except..else语句
# 上面我们说了如果程序运行出错就执行except，那么如果没出错我们应该也有一种语法去接收没有报错的写法。
# 接下来我们将讲的else语句就是写：如果没报错，执行else
# try:
#     b = 0
#     a = b
#     print(a)
# except Exception as e:
#     print(repr(e))
# else:
#     print("No error")
#7.try...except...finally语句
# 写了错或不错的写法，那么现在是剩下不管会不会出错，都会执行的语句
# finally语句则是用于  ： 无论程序报不报错，都将要执行的语句
# try:
#     b = 0
#     a = b
#     print(a)
# except Exception as e:
#     print(repr(e))
# else:
#     print("No error")
# finally:
#     print("Finish!")

# Python高级知识拓展 **选学
# Python高级知识不仅为这2个，还有例如面向对象封装、闭包，迭代器装饰器等等，
# 本处我们选讲条件表达式和生成式以便于我们方便我们实际使用）

# 条件表达式
# 我们通常的条件就是if...else语句组成，但通常都是if ...else语句一句一行，
# 所以我们这里讲述的就是将if else放置在一起简单判断。
# 1.条件表达式
# a = 1
# b = 2
# c  =  a  if  a>b  else  b  # 先执行中间的if，如果返回True，就是if ，False为else。即，如果a>b成立，则c = a,否则c = b
# print(c)
# 2.二维列表表达式
# a = 1
# b = 2
# c = [b, a][a > b]
# m = 3
# n = 2
# d = [n,m][m > n]
# print(c)
# print(d)
# 实际是[b,a][False]，因为False被转换为0，所以是[2,1][0]，也就是[1];[b,a]
# 判断结果 True 返回前面列表第二个， False返回第一个。
# 3.bool 条件表达式（较难）
# a = 1
# b = 2
# c = ( a>b and [a] or [b])[0]
# print(c)
# 转化：False and [1] or [2]，因为and的优先级高于or，先算and
# False和[1] and之后是False，和[2]or之后成了[2]  and >> c = False = 1;  or>>>c=1>>>b=2
# True 和[1] and之后是[1]，但[1]和[2]or结果是[1]
# 基础的3种类型写完了，你学废了嘛？这种写法理解即可，可用在读程序当中，也欢迎在实际写程序时运用，可以大大减少代码量。

# 条件生成式(推导式)
# 生成式又称推导式、解析式，是 python 的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列。
# 例如：当我们需要生成一个字典需要往里面存放内容时，
# 我们通常使用for...in range()方法生成内容存放进去。那么我们现在讲的是如果更快的生成。
# 将10以内所有整数写入列表
# list = [[i for i in range(11)]]
# print(list)  # 列表 i ，用for 循环往 列表i 里面赋值
# 将10以内所有整数的平方写入列表。
# lst = [i**2 for i in range(1, 11)]
# print(lst)
#  条件写入
# 构建一个列表,要求元素大于4
# lst = [i for i in range(11) if i > 4]
# print(lst)
# 有一列表 lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ，取出 1/4/7 和 1/5/9元素
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst1 = [lst[i][0] for i in range(len(lst))]
# print(lst1)
# lst2 = [lst[i][i] or i in range(len(lst))]
# print(lst2)
print("helloWorld")