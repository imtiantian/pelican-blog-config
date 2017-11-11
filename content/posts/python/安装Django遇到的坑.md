Title: 安装Django遇到的坑
Date: 2016-08-05 09:20
Tags: python, django



用`django-admin.py startproject your-project`命令创建项目
>报错：ImportError: No module named django.core

明明已经安装好了Django，却提示没有Django模块，搞什么鬼？
最后查阅资料发现，是因为安装了多个版本Python。
**解决办法：**
~~~
python3 /usr/local/python3.5.2/lib/python3.5/site-packages/django/bin/django-admin.py startproject your-project
~~~
>注意：对于window用户，卸载其他版本Python，也可解决问题；但linux用户，万万不可卸载其他版本的Python，必须用上面方法解决。

* * * * *

配置MySQL数据库，用‘pip3 install PyMySQL’命令安装了pymysql扩展，却还是报错
>报错：No module named 'MySQLdb'

在__init__.py文件中添加下面代码，即可解决：
~~~
import pymysql
pymysql.install_as_MySQLdb()
~~~

* * * * *

为了方便测试，在服务器上`python manage.py runserver 0.0.0.0:8080`，外网却不能通过服务器ip访问，也不报错，后来发现是防火墙的原因，除了指定的端口外，其他端口访问都会被防火墙拒绝，解决办法：
~~~
iptables -I INPUT 4 -p tcp -m state --state NEW -m tcp --dport 8080 -j ACCEPT
~~~
允许 8080 端口
~~~
service iptables save
~~~
保存 iptables 规则

* * * * *

然后再通过“http://139.196.++.+++:8080” 访问，报错了：
>报错：You may need to add '139.196.++.+++' to ALLOWED_HOSTS.

解决办法：在setting.py文件中，找到`ALLOWED_HOSTS = []`,在“[]”中添加你的服务器外网ip地址，如：
~~~
ALLOWED_HOSTS = ['139.196.++.+++']
~~~
然后在你本机，通过“http://服务器ip:8080” 就可以访问你服务器上面的Django项目啦