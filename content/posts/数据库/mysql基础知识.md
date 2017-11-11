Title: mysql基础知识
Date: 2015-10-11 13:36
Tags: 数据库,mysql



**一.数据库的连接**
~~~
mysql -u -p -h
-u 用户名
-p 密码
-h host主机
~~~

* * * * *

**二.修改MySQL提示符**

1.连接客户端时，通过参数指定
~~~
mysql -h localhost -u root --prompt 提示符
~~~
2.连接上客户端后，通过`prompt`命令修改
~~~
prompt 提示符
~~~

######**MySQL提示符**
| 参数   |  描述  |
| --- | --- |
|  \D  |  完整的日期  |
|  \d  |  当前数据库  |
|  \h  |  服务器名称  |
|  \u  |  当前用户  |

* * * * *

**三.库级知识**

1 显示数据库: `show databases`;
2 选择数据库: `use dbname`;
3 创建数据库: `create database dbname charset utf8`;
4 删除数据库: `drop database dbname`;
* * * * *

**四. 表级操作**

1 显示库下面的表: `show tables`;
2 查看表的结构: `desc tableName`;
3 查看表的创建过程: `show create table  tableName`;
4 创建表:
~~~
　create table tbName (
列名称1　列类型　[列参数]　[not null default ],
....列2...
....
列名称N　列类型　[列参数]　[not null default ]
)engine myisam/innodb charset utf8/gbk
~~~
例子:
~~~
create table user (
    id int auto_increment,
    name varchar(20) not null default '',
    age tinyint unsigned not null default 0,
   index id (id)
   )engine=innodb charset=utf8;
~~~
> 注：innodb是表引擎,也可以是myisam或其他,但最常用的是myisam和innodb,charset 常用的有utf8,gbk;

5 修改表
（1）修改表之增加列:

~~~
alter table tbName
add 列名称１　列类型　[列参数]　[not null default ]　
~~~
> 注：add之后的旧列名之后的语法和创建表时的列声明一样

（2）修改表之修改列
~~~
alter table tbName
change 旧列名  新列名  列类型　[列参数]　[not null default ]
~~~
> 注：旧列名之后的语法和创建表时的列声明一样

（3）修改表之减少列:
alter table tbName
drop 列名称;

（4）修改表之增加主键
~~~
alter table tbName add primary key(主键所在列名);
~~~
例:
~~~
alter table goods add primary key(id)
~~~
该例是把主键建立在id列上

（5）修改表之删除主键
~~~
alter table tbName　drop primary key;
~~~

（6）修改表之增加索引
~~~
alter table tbName add [unique|fulltext] index 索引名(列名);
~~~

（7）修改表之删除索引
~~~
alter table tbName drop index 索引名;
~~~

（8）清空表的数据
~~~
truncate tableName;
~~~

* * * * *

**五.列类型讲解**
整型:
~~~
tinyint (0~255/-128~127) smallint (0~65535/-32768~32767) mediumint int bigint

参数解释:
        unsigned 无符号(不能为负)  zerofill 0填充  M 填充后的宽度
        举例:tinyint unsigned;tinyint(6) zerofill;
~~~

数值型
~~~
        浮点型:float double
        格式:float(M,D)  unsigned\zerofill;
~~~

字符型
~~~
        char(m) 定长
        varchar(m)变长
        text
~~~

日期时间类型
~~~
year       YYYY	范围:1901~2155. 可输入值2位和4位(如98,2012)
date       YYYY-MM-DD 如:2010-03-14
time       HH:MM:SS	如:19:26:32
datetime   YYYY-MM-DD  HH:MM:SS 如:2010-03-14 19:26:32
timestamp  YYYY-MM-DD  HH:MM:SS 特性:不用赋值,该列会为自己赋当前的具体时间
~~~

* * * * *
**六.增删改查**

1.插入数据
~~~
	insert into 表名(col1,col2,……) values(val1,val2……); -- 插入指定列
	insert into 表名 values (,,,,); -- 插入所有列
	insert into 表名 values	-- 一次插入多行
	(val1,val2……),
	(val1,val2……),
	(val1,val2……);
~~~

2.修改数据
~~~
	update tablename set
    col1=newval1,
	col2=newval2,
	...
	...
	colN=newvalN
	where 条件;
~~~

3.删除数据
~~~
delete from tablenaeme where 条件;
~~~

4.select     查询

  （1）  条件查询   where
~~~
  1 比较运算符  = ，!=，< > <=  >=
  2 like , not like ('%'匹配任意多个字符,'_'匹配任意单个字符)
  3 in , not in , between and
  4 is null , is not null
~~~


  （2）  分组       `group by `一般要配合5个聚合函数使用:`max,min,sum,avg,count`

  （3）  筛选       `having`
  （4）  排序       `order by`
  （5）  限制       `limit`

* * * * *

**七.连接查询**

1.左连接
~~~
	.. left join .. on
	table A left join table B on tableA.col1 = tableB.col2 ;
~~~
  例句:
~~~
  select 列名 from table A left join table B on tableA.col1 = tableB.col2
~~~
2.右链接: `right join`

3.内连接:  `inner join`

> 左右连接都是以在左边的表的数据为准,沿着左表查右表.
> 内连接是以两张表都有的共同部分数据为准,也就是左右连接的数据之交集.

* * * * *

**八.子查询**
  where 型子查询:内层sql的返回值在where后作为条件表达式的一部分
  例句:
~~~
  select * from tableA where colA = (select colB from tableB where ...);
~~~
  from 型子查询:内层sql查询结果,作为一张表,供外层的sql语句再次查询
  例句:
~~~
  select * from (select * from ...) as tableName where ....
~~~

* * * * *

**存储引擎**
~~~
engine=Myisam\Innodb
~~~
  1 Myisam  速度快 不支持事务 回滚
  2 Innodb  速度慢 支持事务,回滚

  ①开启事务          `start transaction`;
  ②运行sql;
  ③提交,同时生效\回滚 `commit\rollback`;

* * * * *

  **触发器 trigger**

  监视地点:表
  监视行为:增 删 改
  触发时间:after\before
  触发事件:增 删 改

  创建触发器语法
~~~
	create trigger tgName
	after/before insert/delete/update
	on tableName
	for each row
	sql; -- 触发语句
~~~

  删除触发器:`drop trigger tgName`;


**索引**

>  提高查询速度,但是降低了增删改的速度,所以使用索引时,要综合考虑.
>  索引不是越多越好,一般我们在常出现于条件表达式中的列加索引.
>  值越分散的列，索引的效果越好

 索引类型
 `primary key`主键索引
` index` 普通索引
 `unique index` 唯一性索引
 `fulltext index` 全文索引

* * * * *

**mysql的常用命令**

显示当前服务器版本 `select version()`;
显示当前日期时间  `select now()`;
显示当前用户      `select user`;

**语法规则**

> 关键字和函数名称全部大写
> 数据库形成、表名称、字段名称全部小写
> SQL语句必须以分号结尾；
