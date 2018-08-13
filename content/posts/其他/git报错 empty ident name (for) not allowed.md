Title: git报错 empty ident name (for) not allowed.md
Date: 2018-01-05 15:47
Tags: git

> 场景：django的web网站，Python命令`git commit`的时候报错:

```
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <job@izwz9jfcqapyvfw5ywg1lgz.(none)>) not allowed
```
这是在提示我要配置git用户名和邮箱


nginx的配置用户如下：
```
user  job job;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;
...
```

可以看到web的访问用户是 job

而job用户已经配置git用户名和邮箱

经测试，在Xshell中执行`git commit`命令也完全没问题

为何在django控制器中执行`git commit`报错，而Xshell中却不报错呢？

找不到原因，但好在有解决办法！在.git/config文件中配置好用户名和邮箱就好了，如下：
```
[user]
    name = 你的名字
    email = 你的邮箱
```