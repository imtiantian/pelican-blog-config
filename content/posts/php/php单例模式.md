Title: php单例模式
Date: 2016-02-11 10:55
Tags: php, 单例模式


通过单例模式获取`Databases`对象
~~~
class Databases
{
    protected $db;//保存当前对象

    private function __construct()
    {
        //私有的构造方法，意在禁止外部直接new Databases()
    }

    /*
     * 实现单列模式
     * 若需要调用对象，则通过下面方法调用
     * */
    static function getDatabases()
    {
        if (self::$db) {
            return self::$db;
        } else {
            return self::$db = new self();
        }
    }
}
~~~

* * * * *
~~~
/*
*工厂模式
**/
class Factory{
	//获取Databases对象
    static function createDatabases(){
        $db = Databases::getDatabases();
        return $db;
    }
}
~~~

* * * * *
~~~
//通过工厂方法调用Databases类
\Factory::createDatabases();
~~~
