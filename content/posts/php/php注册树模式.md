Title: php注册树模式
Date: 2016-02-12 09:22
Tags: php, 注册树模式



一个对象，可能很多地方需要用到；每用到一次，就new一次，浪费资源。通过注册器模式，初始化的时候注册对象，往后就可以直接获取注册器中的对象，而不用再new。
**1. 注册器类**
~~~
/*
*注册树模式
**/
class Register{
    protected static $objects;//对象数组

    /*
     * 注册对象
     * */
    static function _set($name,$object){
        self::$objects[$name] = $object;
    }

    /*
     * 获取对象
     * */
    static function _get($name){
        return self::$objects[$name];
    }

    /*
     * 删除对象
     * */
    static function _unset($name){
        unset(self::$objects[$name]);
    }
}
~~~

* * * * *
**2. 注册databases对象的方法**
~~~
/*
*工厂模式
**/
class Factory{
    static function createDatabases(){
        $db = Databases::getDatabases();
        Register::_set('databases',$db);//注册databases对象
    }
}
~~~

* * * * *
**3. 注册databases对象**
~~~
\Factory::createDatabases();
~~~

* * * * *
**4. 通过注册器，获取databases对象**
~~~
\Register::_get('databases');
~~~

* * * * *
> 初始化时，调用“\Factroy::createDatabase()”，注册databases对象; 然后就可以在任何地方通过直接“\Register::get('databases')”，获取databases对象；

* * * * *

> 也就是初始化时只需调用一次“\Factroy::createDatabase()”，往后不用再调用“\Factroy::createDatabase()”方法了，直接“IMooc\Register::get('databases')”获取；