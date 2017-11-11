Title: php适配器模式
Date: 2016-02-13 12:45
Tags: php, 适配器模式



像thinkphp，执行一个数据库查询操作；
~~~
D('User')->field('id,name')->where(['age'=>['lt',18]])->order('age desc')->select();
~~~
无论你是使用**pdo**或是**mysqli**还或是**其他**连接方式操作数据库，查询语句始终是上面那样。

* * * * *
**数据库接口**
~~~
interface Databases{
    //数据库连接
    function connent($host,$dbname,$user,$password);

    //数据库查询
    function query($sql);

    //关闭数据库连接
    function close();
}
~~~

* * * * *
**pdo连接操作数据库**
~~~
class Pdo implements Databases{
    protected $conn;//保存当前对象
    function connent($host,$dbname,$user,$password)
    {
        // TODO: Implement connent() method.
        $conn = new \PDO("mysql:dbname=$dbname;host=$host",$user,$password);
        $this->conn = $conn;
        return $this;
    }

    function query($sql)
    {
        // TODO: Implement query() method.
        $result = $this->conn->query($sql);
        $row = $result->fetch();
        return $row;
    }

    function close()
    {
        // TODO: Implement close() method.
        mysqli_close($this->conn);
    }
}
~~~

* * * * *
**mysqli连接操作数据库**
~~~
class Mysqli implements Databases{
    protected $conn;//保存当前对象
    function connent($host,$dbname,$user,$password)
    {
        // TODO: Implement connent() method.
        $conn = mysqli_connect($host,$user,$password,$dbname);
        $this->conn = $conn;
        return $this;
    }

    function query($sql)
    {
        // TODO: Implement query() method.
        $result = mysqli_query($this->conn,$sql);
        $row = mysqli_fetch_all($result);
        return $row;
    }

    function close()
    {
        // TODO: Implement close() method.
        mysqli_close($this->conn);
    }
}
~~~

* * * * *
**查询操作**
~~~
//$db = new Db\Pdo();
$db = new Db\Mysqli();
$result = $db->connent('127.0.0.1','blog','root','123456')->query();
~~~