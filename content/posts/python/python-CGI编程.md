Title: python-CGI编程
Date: 2016-10-09 10:20
Tags: python, cgi


* 找到下面行：
~~~
AddHandler cgi-script .cgi
~~~
去掉前面的#，在后面加上`.py`,如下：
~~~
AddHandler cgi-script .cgi .py
~~~

* * * * *

* 找到下面行：
~~~
 Options +Indexes +FollowSymLinks
~~~
在后面加上`+ExecCGI`,如下：
~~~
Options +Indexes +FollowSymLinks +Multiviews +ExecCGI
~~~

* * * * *

* 保存，重启apache。

* * * * *
* 在index.py文件中添加如下：
~~~
#!D:\python\python.exe
# -*- coding: UTF-8 -*-

print ('Status: 200 OK')
print ('Content-type: text/html')
print ('')

print ("Hello word!")
~~~
>上面代码除了最后一行以外，其他都必须；
>第一行写明python路径，下面要返回http头信息；
>然后再打印一个空字符串；
>最后一行输出你想要输出的内容。