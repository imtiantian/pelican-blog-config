Title: php策略模式
Date: 2016-02-15 15:57
Tags: php, 策略模式



需求：对于不同的用户展示不同的内容

* * * * *
**定义接口**
~~~
interface UserStrategy{
    function showAd();//展示广告
    function showCategory();//展示分类
}
~~~

* * * * *
**普通用户展示的内容**
~~~
class CommonUser implements UserStrategy{
    public function showAd()
    {
        // TODO: Implement showAd() method.
        //展示普通用户广告
    }
    public function showCategory()
    {
        // TODO: Implement showCategory() method.
        //展示普通用户商品分类
    }
}
~~~

* * * * *
**vip用户展示的内容**
~~~
class VipUser implements UserStrategy{
    public function showAd()
    {
        // TODO: Implement showAd() method.
        //展示会员广告
    }
    public function showCategory()
    {
        // TODO: Implement showCategory() method.
        //展示会员商品分类
    }
}
~~~

* * * * *
**设置用户对象，展示用户页面**
~~~
class UserPage{
    protected $user_object;//用户对象，vip用户或普通用户

    /*
     * 设置用户对象
     * */
    function strategy(UserStrategy $strategy){
        $this->user_object = $strategy;
    }

    function index(){
        $ad = $this->user_object->showAd();//获取广告
        $category = $this->user_object->showAd();//获取商品分类
    }
}
~~~

* * * * *
**根据不同用户，展示不同界面**
~~~
if($is_vip == true){
    $strategy = new \VipUser();
}else{
    $strategy = new \CommonUser();
}
$user_page = new UserPage();
$user_page->strategy($strategy)->index();
~~~