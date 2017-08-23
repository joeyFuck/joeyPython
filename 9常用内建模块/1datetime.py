# datetime是Python处理日期和时间的标准库。

from datetime import datetime # 如果仅导入import datetime，则必须引用全名datetime.datetime。
now = datetime.now()
print(now)
print(type(now))

# datetime转换为timestamp
#
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
# 当前时间就是相对于epoch time的秒数，称为timestamp。
now_time_span = now.timestamp ()  # 把datetime转换为timestamp
print(now_time_span)
# 从timestamp转换到datetime
print(datetime.fromtimestamp(now_time_span))
# timestamp也可以直接被转换到UTC标准时区的时间：(北京时区-8)
print(datetime.utcfromtimestamp(now_time_span))
# 字符串转日期  字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。  注意转换后的datetime是没有时区信息的
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 日期转字符串
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减

from datetime import datetime, timedelta

#datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))



















