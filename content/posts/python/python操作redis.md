Title: python操作redis
Date: 2017-11-18 14:57
Tags: python, redis

## 数据类型
Redis支持五种数据类型：`string`（字符串），`hash`（哈希），`list`（列表），`set`（集合）及`zset`(sorted set：有序集合)。

### 1.`String`（字符串）操作
> redis中的String在在内存中按照一个name对应一个value来存储

`set(name, value, ex=None, px=None, nx=False, xx=False)`
在Redis中设置值，不存在则创建，存在则修改

参数 | 意义
---|---
ex|过期时间（秒）
px|过期时间（毫秒）
nx|如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
xx|如果设置为True，则只有name存在时，当前set操作才执行

`setex(name, value, time)` 设置过期时间（秒）

`psetex(name, time_ms, value)` 设置过期时间（豪秒）

`mset(name1='***', name2='***',......)` 批量设置值

`get(name)` 获取值

`mget(*keys)` 批量获取值

`getset(name, value)` 设置新值，打印原值

`getrange(key, start, end)` 获取值,并切片，返回切片后的结果

`setrange(name, offset, value)` 修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加

`setbit(name, offset, value)` 对二进制表示位进行操作

`getbit(name, offset)` 获取name对应值的二进制中某位的值(0或1)

`bitcount(key, start=None, end=None)` 获取对应二进制中1的个数

`strlen(name)` 返回name对应值的字节长度（一个汉字3个字节）

`incr(name, amount=1)` 自增name对应的值，当name不存在时，则创建name＝amount，否则，则自增,amount为自增数(整数)

`incrbyfloat(name, amount=1.0)` 类似`incr()`自增,amount为自增数(浮点数)

`decr(name, amount=1)` 自减name对应的值,当name不存在时,则创建name＝amount，否则，则自减，amount为自增数(整数)

`append(name, value)` 在name对应的值后面追加内容

### 2.`Hash`（哈希）操作
> redis中的Hash 在内存中类似于一个name对应一个dic来存储

`hset(name, key, value)` name对应的hash中设置一个键值对。不存在，则创建，否则，修改。

`hget(name,key)` 在name对应的hash中根据key获取value

`hgetall(name)` 获取name对应hash的所有键值

`hmset(name, dict)` 在name对应的hash中批量设置键值对

`hmget(name, keys)` 在name对应的hash中获取多个key的值

`hlen(name)` 获取hash中键值对的个数

`hkeys(name)` 获取hash中所有的key的值

`hvals(name)` 获取hash中所有的value的值

`hexists(name, key)` 检查name对应的hash是否存在当前传入的key

`hdel(name,*keys)` 删除指定name对应的key所在的键值对

`hincrby(name, key, amount)` 自增hash中key对应的值，不存在则创建key=amount(amount为整数)

`hincrbyfloat(name, key, amount)` 自增hash中key对应的值，不存在则创建key=amount(amount为浮点数)

`hscan(name, cursor=0, match=None, count=None)`

`hscan_iter(name, match=None, count=None)`

### `List`（列表）操作

> redis中的List在在内存中按照一个name对应一个List来存储

`lpush(name,*values)` 在name对应的list中添加元素，每个新的元素都添加到列表的最左边

`rpush(name,*values)` 同`lpush`，但每个新的元素都添加到列表的最右边

`lpushx(name,value)` 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边

`rpushx(name,value)` 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最右边

`llen(name)` name对应的list元素的个数

`linsert(name, where, refvalue, value))` 在name对应的列表的某一个值前或后插入一个新值

参数 | 意义
---|---
name|redis的name
where|BEFORE（前）或AFTER（后）
refvalue|列表内的值
value|要插入的数据

`r.lset(name, index, value)` 对list中的某一个索引位置重新赋值

`lrem(name, value, num)` 删除name对应的list中的指定值
```
name  ---  redis的name
value ---  要删除的值
num   ---  num为0，表示删除列表中所有的指定值；
           num为n，表示从前到后删除n个；
           num为-n：从后向前删除n个
```

`lpop(name)` 移除列表的左侧第一个元素，返回值是移除的元素

`lindex(name, index)` 根据索引获取列表内元素

`lrange(name, start, end)` 分片获取元素

`ltrim(name, start, end)` 移除列表内没有在该索引之内的值

`rpoplpush(src, dst)` # 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边，src要取数据的列表，dst要添加数据的列表

`brpoplpush(src, dst, timeout=0)` 同rpoplpush，多了个timeout, timeout：取数据的列表没元素后的阻塞时间，0为一直阻塞

`blpop(keys, timeout)` 将多个列表排列,按照从左到右去移除各个列表内的元素；timeout: 超时时间，获取完所有列表的元素之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞

`brpop(keys, timeout)` 同blpop，将多个列表排列,按照从右像左去移除各个列表内的元素

### `Set`（集合）操作

> Set集合就是不允许重复的列表

`sadd(name,*values)` 给name对应的集合中添加元素

`smembers(name)` 获取name对应的集合的所有成员

`scard(name)` 获取name对应的集合中的元素个数

`sdiff(name, *names)` 在第一个name对应的集合中且不在其他name对应的集合的元素集合

例：
```
import redis,time

r = redis.Redis(host='127.0.0.1', port=6379)
r.sadd("name","a","b")
r.sadd("name1","b","c")
r.sadd("name2","b","c","d")
print(r.sdiff("name","name1","name2"))#输出:｛a｝
```

`sdiffstore(dest, name, *names)` 相当于把`sdiff`获取的值加入到dest对应的集合中

`sinter(*names)` 获取多个name对应集合的交集

例：
```
import redis,time

r = redis.Redis(host='127.0.0.1', port=6379)
r.sadd("name","a","b")
r.sadd("name1","b","c")
r.sadd("name2","b","c","d")
print(r.sinter("name","name1","name2"))#输出:｛b｝
```

`sinterstore(dest, name, *names)` 获取多个name对应集合的交集，再讲其加入到dest对应的集合中；相当于把`sinter`获取的值加入到dest对应的集合中

`sismember(name, value)` 检查value是否是name对应的集合内的元素

`smove(src, dst, value)` 将某个元素从一个集合中移动到另外一个集合

`spop(name)` 从集合的右侧移除一个元素，并将其返回

`srandmember(name, numbers)` 从name对应的集合中随机获取numbers个元素

`srem(name, *values)` 删除name对应的集合中的某些值

`sunion(*names)` 获取多个name对应的集合的并集

`sunionstore(dest,*names)` 获取多个name对应的集合的并集，并将结果保存到dest对应的集合中

### `zset`（有序集合）

> 在集合的基础上，为每元素排序，元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序

`zadd(name, *args, **kwargs)` 在name对应的有序集合中添加元素

`zcard(name)` 获取有序集合内元素的数量

`zcount(name, min, max)` 获取有序集合中分数在min~max之间的个数

`zincrby(name, value, amount)` 自增有序集合内value对应的分数

`zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)` 按照索引范围获取name对应的有序集合的元素

参数 | 意义
---|---
name|redis的name
start|有序集合索引起始位置
end|有序集合索引结束位置
desc|排序规则，默认按照分数从小到大排序
withscores|是否获取元素的分数，默认只获取元素的值
score_cast_func|对分数进行数据转换的函数

`zrevrange(name, start, end, withscores=False, score_cast_func=float)` 同`zrange`，集合是从大到小排序的

`zrank(name, value)` 获取value值在name对应的有序集合中的排行位置（从0开始）

`zrevrank(name, value)` 同`zrank`，集合是从大到小排序的

`zscore(name, value)` 获取name对应有序集合中 value 对应的分数

`zrem(name, *values)` 删除name对应的有序集合中值是values的成员

`zremrangebyrank(name, min, max)` 根据排行范围删除

`zremrangebyscore(name, min, max)` 根据分数范围删除

`zinterstore(dest, *keys, aggregate=None)` 获取两个有序集合的交集并放入dest集合，如果遇到相同值不同分数，则按照aggregate进行操作。aggregate的值为: SUM  MIN  MAX

`zunionstore(dest, keys, aggregate=None)` 获取两个有序集合的并集并放入dest集合，其他同`zinterstore`

---

## 其他常用操作

`delete(*names)` 根据name删除redis中的任意数据类型

`exists(name)` 检测redis的name是否存在

`keys(pattern='*')` 根据* ？等通配符匹配获取redis的name

`expire(name ,time)` 为某个name设置超时时间

`rename(src, dst)` 重命名

`move(name, db))` 将redis的某个值移动到指定的db下

`randomkey()` 随机获取一个redis的name（不删除）

`type(name)` 获取name对应值的类型