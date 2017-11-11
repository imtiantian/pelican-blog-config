Title: php观察者模式
Date: 2016-02-20 13:08
Tags: php, 观察者模式



当发生一个事件后，可能需要执行多种业务的逻辑操作，这里的每一种逻辑都是一个观察者。
* * * * *

**观察者基类**
~~~
abstract class EventGenerator{
    private $observers = [];//观察者对象数组

    /*
     * 添加观察者
     * */
    function addObserver(Observer $observer){
        $this->observers[] = $observer;
    }

    /*
     * 通知观察者
     * */
    function notify(){
        foreach ($this->observers as $observer){
            $observer->logic();
        }
    }
}
~~~

* * * * *
**观察者接口**
~~~
interface Observer{
    function logic($event_info='');
}
~~~

* * * * *
**触发事件，通知观察者的类**
~~~
class Event extends EventGenerator{
    function trigger(){
        echo 'Event';//触发了一个事件
        $this->notify();//通知观察者
    }
}
~~~

* * * * *
**这是一个观察者**
~~~
class ObserverOne implements Observer{
    function logic($event_info=''){
        echo '逻辑一';
    }
}
~~~

* * * * *
**触发事件**
~~~
$event = new \Event();
$event->addObserver(new \ObserverOne());//添加观察者
$event->trigger();//触发事件
~~~