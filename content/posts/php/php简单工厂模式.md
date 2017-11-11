Title: php简单工厂模式
Date: 2016-02-18 16:34
Tags: php, 工厂模式



有个**Databases**类，传统用法是，哪里需要，哪里`new Databases;`;这样若**Databases**对象发生了改变，则有实例化**Databases**的地方都要相应改变。

采用工厂模式实现：
~~~
/*
*工厂模式
**/
class Factory{
    static function createDatabases(){
        $Databases = new Databases();
        return $Databases;
    }
}
~~~

* * * * *

~~~
//通过工厂方法调用Databases类
\Factory::createDatabases();
~~~

* * * * *
> 好处：当我们对象所对应的类的类名发生变化的时候，我们只需要改一下工厂类类里面的实例化方法即可。不需要外部改所有的地方