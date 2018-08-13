Title: crontab定时任务
Date: 2017-03-22 15:36
Tags: linux,crontab,定时任务


### crontab配置文件格式
```
*  *  *  *  *  COMMAND
|  |  |  |  |
|  |  |  |  |__星期0~7，（0或7表示星期天）
|  |  |  |_____月份1~12
|  |  |________日期1~31
|  |___________小时0~23
|______________分钟0~59
```

```
小结：
*表示任何时候都匹配
可以用“A,B,C”表示A或者B或者C时执行命令
可以用“A-B”表示A到B之间时执行命令
可以用“\*/A”表示每A分钟（小时）等执行一次命令
```

### crontab举例：
每晚21:30重启Apache
```
30 21 * * * service httpd restart
```

每月1,10,24号的4:45重启Apach
```
45 4 1,10,24 * * service httpd restart
```

每月1到10号的4:45重启Apache
```
45 4 1-10 * * service httpd restart
```

每隔两分钟重启Apache
```
*/2 * * * * service httpd restart

1-59/2 * * * * service httpd restart
```

晚上11点到早上7点之间，每隔一小时重启Apache
```
0 23-7/1 * * * service httpd restart
```

每天18:00到23:00之间，每隔30分钟重启Apache
```
0,30 18-23 * * * service httpd restart

0-59/30 18-23 * * * service httpd restart
```