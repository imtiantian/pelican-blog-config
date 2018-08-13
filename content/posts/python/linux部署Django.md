Title: linux部署Django
Date: 2016-10-09 10:20
Tags: python, django,linux



首先，安装uwsgi,命令`pip3 install uwsgi`;

在nginx.conf配置文件中，`http{}`的最后加上一行：
~~~
include vhost/*.conf;
~~~
目的是引入vhost文件夹下的配置文件；
在**nginx.conf**同目录下创建**vhost**文件夹，用来专门存放你的各种项目应用的配置文件。

* * * * *
假设你已经创建好了Django应用，名字叫‘djangoceshi’；在**vhost**文件夹下新建**djangoceshi.conf**文件，内容：
~~~
upstream djangoceshi {
  server unix:///tmp/djangoceshi.sock;
}
server {
    listen 80;
    server_name djangoceshi.xzwphp.com;
    access_log /data/wwwlogs/djangoceshi.xzwphp.com_nginx.log combined;
    index index.html index.htm index.py;
    #include /usr/local/nginx/conf/rewrite/djangoceshi.conf;
    charset utf-8;
    client_max_body_size 75M;


  location /media {
      alias /data/wwwroot/djangoceshi/media;
  }

  location /static {
      alias /data/wwwroot/djangoceshi/static;
  }

  location / {
    uwsgi_pass djangoceshi;
    include uwsgi_params;
  }
}
~~~
* `#include /usr/local/nginx/conf/rewrite/djangoceshi.conf;`这一行引入的是你的**dangoceshi**的路由规则，我在这里注释掉了。
* `server_name djangoceshi.xzwphp.com;`这一行是你解析到服务器ip的域名。
* `charset utf-8;`指定编码。
* `client_max_body_size 75M;`指定最大上传尺寸。
* `alias /data/wwwroot/djangoceshi/media;`指定你的媒体文件目录。
* `alias /data/wwwroot/djangoceshi/static;`指定你的项目的静态资源文件目录，css，js等。

* * * * *
运行命令`nginx -t`，查看配置是否有语法错误；然后再输入命令‘nginx -s reload’使修改的配置生效。

* * * * *


在你的项目所在文件夹，和**manage.py**同目录，创建djangoceshi.ini文件，内容：
~~~
[uwsgi]

chdir = /data/wwwroot/djangoceshi
module = djangoceshi.wsgi

master = true
processes = 10

socket = /tmp/djangoceshi.sock
chmod-socket = 664

vacuum = true

daemonize=/data/nginx/wsgilogs/djangoceshi.log
~~~
* `module = djangoceshi.wsgi`引入你项目的wsgi.py文件。
* `chdir = /data/wwwroot/djangoceshi`这里写上你项目的所在目录。
* `daemonize=/data/nginx/wsgilogs/djangoceshi.log`记录你项目的uwsgi的运行记录，需要先建好文件夹，不然会报错，找不到目录，我的文件夹是**/data/nginx/wsgilogs/**。

* * * * *
启动uwsgi：
~~~
uwsgi3 --ini /data/wwwroot/djangoceshi/djangoceshi.ini
~~~

然后访问域名**djangoceshi.xzwphp.com**，发现不成功，查看记录文件**djangoceshi.log**发现，报了一个错误：
~~~
Sun Dec  4 12:57:43 2016 - *** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
~~~

* * * * *

解决办法：
创建**www**用户组和**www**用户；
~~~
/usr/sbin/groupadd www
/usr/sbin/useradd -g www www
~~~

编辑Nginx的配置文件**nginx.conf**，将第一行修改为`user www www;`
去掉下面两行注释：
~~~
#error_log  logs/error.log;
#pid        logs/nginx.pid;
~~~

在**djangoceshi.ini**文件中添加两行：
~~~
uid = www
gid = www
~~~
如：
~~~
[uwsgi]
uid = www
gid = www

chdir = /data/wwwroot/djangoceshi

......
~~~

再输入命令`nginx -s reload`使修改**nginx.conf**的配置生效;
启动uwsgi,`uwsgi --ini /data/wwwroot/djangoceshi/djangoceshi.ini`.