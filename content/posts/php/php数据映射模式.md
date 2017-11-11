Title: php数据映射模式
Date: 2016-02-16 14:44
Tags: php, 数据映射模式



**获取用户id为$id的用户对象**
~~~
/*
*数据映射模式
**/
class User{
	//这里的id,name,age属性和数据库中的字段相对应
    public $id;
    public $name;
    public $age;
    protected $db;

    function __construct($id)
    {
        $this->id = $id;
        $this->db = new Db\Pdo();
        $user = $this->db->connent('127.0.0.1','blog','root','123456')->query("select * from user where id={$id}");
        $this->name = $user['name'];
        $this->age = $user['age'];
    }

	//这里实现当对象属性改变时，实现数据库修改
    function __destruct()
    {
        $this->db->query("update user set name={$this->name},age={$this->age} where id={$this->id}");
    }
}
~~~
* * * * *
**注册id为$id的用户对象**
~~~
/*
*工厂模式
**/
class Factory{
    static function createUser($id){
        $user = new User($id);
        Register::_set('user',$user);//注册User对象
    }
}
~~~

* * * * *
**实现用户对象修改**
~~~
\Factory::createUser(1);//调用工厂方法，注册id为1的用户对象
$user = \Register::_get('user');获取用户对象

//这里修改id为1的用户对象的某个属性后，就会调用对象的析构方法，改变数据库相应字段
$user->name = 'tiantian';//修改用户姓名
$user->age = 18;//修改用户年龄
~~~