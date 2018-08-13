Title: dateutil库（datetime模块的扩展）
Date: 2017-12-08 14:43
Tags: python


最近经常需要用Python计算时间日期，如：计算两个日期间的日期列表，函数如下：
```
from datetime import datetime,timedelta

def get_date_among_two_date(start_date,end_date):
    a_day = timedelta(days=1)

    res = []
    while start_date <= end_date:
        res.append(start_date)
        start_date += a_day
    return res

```

后来了解到了`dateutil`库，发现用`dateutil`库实现更为简单,实现如下：
```
from dateutil.rrule import *

def get_date_among_two_date(start_date,end_date):
    return list(rrule(DAILY,dtstart=start_date,until=end_date))
```
---
### `dateutil`用法
#### `relativedelta`（时间偏移）
例：
```
from datetime import datetime;
from dateutil.relativedelta import relativedelta

#计算指定日期与现在的差值
now_date = datetime.now()
relativedelta(datetime(2003, 10, 24, 10, 0), now_date)
'''
结果：relativedelta(years=-14, months=-1, days=-15, hours=-5, minutes=-33, seconds=-38, microseconds=+866005)
'''

#计算下个月的今天
datetime.today()+relativelta(months=+1)
```
---
#### `parser`（根据字符串解析成datetime）
例：
```
from dateutil import parser
parser.parse("2003-09-25T10:49:41")

parser.parse("20030925T104941")

#fuzzy开启模糊匹配，过滤掉无法识别的时间日期字符
parse("this is 12:00:00",fuzzy=True)

'''
fuzzy_with_tokens开启模糊匹配,返回一个元组
其中第一个元素是已解析的datetime
第二个元素是一个包含被忽略的字符串的部分的元组
'''
parse('this is 12:00:00',fuzzy_with_tokens =True)

```
---
#### `rrule`（根据定义的规则来生成datetime）

>class dateutil.rrule.rrule(freq, dtstart=None, interval=1, wkst=None, count=None, until=None, bysetpos=None, bymonth=None, bymonthday=None, byyearday=None, byeaster=None, byweekno=None, byweekday=None, byhour=None, byminute=None, bysecond=None, cache=False)


freq --- 时间单位。可以是 YEARLY, MONTHLY, WEEKLY, DAILY,HOURLY, MINUTELY, SECONDLY。即年月日周时分秒。

dtstart --- 开始时间

until --- 结束时间

wkst --- 周开始时间。

interval --- 间隔。

count --- 指定生成多少个。

by*** --- 指定匹配的周期。比如byweekday=(MO,TU)则只有周一周二的匹配。byweekday可以指定MO,TU,WE,TH,FR,SA,SU。即周一到周日。

例：
```
from dateutil.rrule import *

#计算两日期之间的日期，间隔为3
list(rrule(DAILY,interval=3,dtstart=parse('2017-12-01'),until=parse('2017-12-24')))

#计算两日期之间的日期，返回前三个
list(rrule(DAILY,count=3,dtstart=parse('2017-12-01')))

#计算两日期之间的周六周天的日期
list(rrule(DAILY,byweekday=(SA,SU),dtstart=parse('2017-12-01'),until=parse('2018-02-24')))

#按月为单位
list(rrule(MONTHLY,dtstart=parse('2017-05-19'),until=parse('2017-12-20')))
```
---
#### [`dateutil`文档地址](http://dateutil.readthedocs.io/)