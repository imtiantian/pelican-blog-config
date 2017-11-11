Title: php常用魔术方法
Date: 2016-06-23 12:33
Tags: php, 魔术方法



~~~
class Ceshi{
    public $array;

    /*
     * 对一个不存在的属性进行赋值时，触发此方法
     * */
    function __set($name, $value)
    {
        // TODO: Implement __set() method.
        $this->array[$name] = $value;

    }

    /*
     * 获取一个不存在的属性时，触发此方法
     * */
    function __get($name)
    {
        // TODO: Implement __get() method.
        return $this->array[$name];
    }

    /*
     *当调用一个不存在的非静态方法时，会触发此函数
     * */
    function __call($name, $arguments)
    {
        // TODO: Implement __call() method.
        echo 'function"'.$name.'"不存在';
    }

    /*
     *当调用一个不存在的静态方法时，会触发此函数
     * */
    static function __callStatic($name, $arguments)
    {
        // TODO: Implement __callStatic() method.
        echo '静态function"'.$name.'"不存在';
    }

    /*
     *当把对象当成字符串直接输出时，会触发此函数
     * */
    function __toString()
    {
        // TODO: Implement __toString() method.
        var_dump($this);
        return '不能直接输出一个对象';
    }

    /*
     * 当把对象当成函数使用时，会触发此函数
     * */
    function __invoke($arguments)
    {
        // TODO: Implement __invoke() method.
        echo '不能把对象当成函数使用';
    }
}
~~~
