# 在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
#
# '00\d'可以匹配'007'，但无法匹配'00A'；
#
# '\d\d\d'可以匹配'010'；
#
# '\w\w\d'可以匹配'py3'；
#
# .可以匹配任意字符，所以：
#
# 'py.'可以匹配'pyc'、'pyo'、'py!'等等。
# 要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
#
# 来看一个复杂的例子：\d{3}\s+\d{3,8}。
#
# 我们来从左到右解读一下：
#
# 1. \d{3}表示匹配3个数字，例如'010'；
#
# 2.\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
#
# 3.\d{3,8}表示3-8个数字，例如'1234567'。
#
# 综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
#
# 如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。



# 进阶!!!!!!!!!!!!!!!
# 要做更精确地匹配，可以用[]表示范围，比如：
#
#-- [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
#
# --[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
#
# --[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
#
# --[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
#
# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
#
# ^表示行的开头，^\d表示必须以数字开头。
#
# $表示行的结束，\d$表示必须以数字结束。
#
# 你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。


# re模块   使用
# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
import  re
s = r'ABC\-001' # Python的字符串
b = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(b)
if b:
    print('ok')
else:
    print('failed')

# 正则用于切分字符串

print('a b   c'.split(' '))
# 嗯，无法识别连续的空格，用正则表达式试试：
print(re.split(r'\s+','a b   c')) # \s+ 匹配至少一个空格
re.split(r'[\s\,]+', 'a,b, c  d') # 加入,
re.split(r'[\s\,\;]+', 'a,b;; c  d') # 加入;

# 分组

# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）

# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0)) # group(0)永远是原始字符串
print(m.group(1))
print(m.group(2))

# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：

re.match(r'^(\d+)(0*)$', '102300').groups()
# ('102300', '')
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
#
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

re.match(r'^(\d+?)(0*)$', '102300').groups()
# ('1023', '00')


# 编译

# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：

# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2.用编译后的正则表达式去匹配字符串。


# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
re_telephone.match('010-12345').groups()
# ('010', '12345')
re_telephone.match('010-8086').groups()
# ('010', '8086')





















