Title: Django配置静态文件目录
Date: 2016-12-22 10:54
Tags: python, django


开发环境配置静态文件目录：

setting.py文件中：
INSTALLED_APPS中加入`django.contrib.staticfiles`；

最后面加上下面代码：

~~~
STATICFILES_DIRS = (
	#这里的"common"是manage.py同目录下存放静态文件的目录，可随意改名
    os.path.join(BASE_DIR, "common"),
    #'D:\WWW\demo\demo1\common',
)
~~~

* * * * *

url.py文件后面加上下面代码：

~~~
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
~~~


* * * * *
这样就已经可以访问静态文件了“http:127.0.0.1:8000/common/00000.css”

* * * * *


为了避免模板中引入静态文件的时候，将路径写死，需配置settings变量的全局引用：
在view 里面引用setting里面的配置信息
~~~
from django.conf import settings
~~~
接着在view里面定义一个函数读取我们的setting文件的变量
~~~
def my_setting(request):
    return {"STATIC_URL":settings.STATIC_URL}
~~~
最后我们需要把这个my_setting 函数的方法加入到们到settings 的 TEMPLATES 的配置项里面
~~~
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'LinkageAndPage.views.my_setting'#在这里
            ],
        },
    },
]
~~~
模板中引入静态资源
~~~
<a href="{{ STATIC_URL }}style.css">这是静态资源</a>
~~~
