Title: php JSON数据格式化方法
Date: 2015-09-09 15:20
Tags: php, json


原文链接：[php JSON数据格式化方法](http://blog.csdn.net/fdipzone/article/details/28766357)

* * * * *

php 的json_encode能把数组转换为json格式的字符串。字符串没有缩进，中文会转为unicode编码，例如\u975a\u4ed4。人阅读比较困难。现在这个方法在json_encode的基础上再进行一次美化处理。使人能方便阅读内容。

* * * * *

**1. 使用 json_encode 输出**
~~~
<?php

header('content-type:application/json;charset=utf8');

$arr = array(
    'status' => true,
    'errMsg' => '',
    'member' =>array(
        array(
            'name' => '李逍遥',
            'gender' => '男'
        ),
        array(
            'name' => '赵灵儿',
            'gender' => '女'
        )
    )
);

echo json_encode($arr);

?>
~~~
**输出：**
~~~
{"status":true,"errMsg":"","member":[{"name":"\u674e\u900d\u9065","gender":"\u7537"},{"name":"\u8d75\u7075\u513f","gender":"\u5973"}]}
~~~
可以看出，这种格式人阅读很困难。


* * * * *

**2. 使用 jsonFormat 输出**
~~~
<?php

/** Json数据格式化
* @param  Mixed  $data   数据
* @param  String $indent 缩进字符，默认4个空格
* @return JSON
*/
function jsonFormat($data, $indent=null){

    // 对数组中每个元素递归进行urlencode操作，保护中文字符
    array_walk_recursive($data, 'jsonFormatProtect');

    // json encode
    $data = json_encode($data);

    // 将urlencode的内容进行urldecode
    $data = urldecode($data);

    // 缩进处理
    $ret = '';
    $pos = 0;
    $length = strlen($data);
    $indent = isset($indent)? $indent : '    ';
    $newline = "\n";
    $prevchar = '';
    $outofquotes = true;

    for($i=0; $i<=$length; $i++){

        $char = substr($data, $i, 1);

        if($char=='"' && $prevchar!='\\'){
            $outofquotes = !$outofquotes;
        }elseif(($char=='}' || $char==']') && $outofquotes){
            $ret .= $newline;
            $pos --;
            for($j=0; $j<$pos; $j++){
                $ret .= $indent;
            }
        }

        $ret .= $char;

        if(($char==',' || $char=='{' || $char=='[') && $outofquotes){
            $ret .= $newline;
            if($char=='{' || $char=='['){
                $pos ++;
            }

            for($j=0; $j<$pos; $j++){
                $ret .= $indent;
            }
        }

        $prevchar = $char;
    }

    return $ret;
}

/** 将数组元素进行urlencode
* @param String $val
*/
function jsonFormatProtect(&$val){
    if($val!==true && $val!==false && $val!==null){
        $val = urlencode($val);
    }
}

header('content-type:application/json;charset=utf8');

$arr = array(
    'status' => true,
    'errMsg' => '',
    'member' =>array(
        array(
            'name' => '李逍遥',
            'gender' => '男'
        ),
        array(
            'name' => '赵灵儿',
            'gender' => '女'
        )
    )
);

echo jsonFormat($arr);

?>
~~~
**输出：**
~~~
{
    "status":true,
    "errMsg":"",
    "member":[
        {
            "name":"李逍遥",
            "gender":"男"
        },
        {
            "name":"赵灵儿",
            "gender":"女"
        }
    ]
}
~~~


* * * * *

php5.4 以后，json_encode增加了JSON_UNESCAPED_UNICODE , JSON_PRETTY_PRINT 等几个常量参数。使显示中文与格式化更方便。

~~~
header('content-type:application/json;charset=utf8');

$arr = array(
    'status' => true,
    'errMsg' => '',
    'member' =>array(
        array(
            'name' => '李逍遥',
            'gender' => '男'
        ),
        array(
            'name' => '赵灵儿',
            'gender' => '女'
        )
    )
);

echo json_encode($arr, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
~~~
**输出：**
~~~
{
    "status": true,
    "errMsg": "",
    "member": [
        {
            "name": "李逍遥",
            "gender": "男"
        },
        {
            "name": "赵灵儿",
            "gender": "女"
        }
    ]
}
~~~


* * * * *

**JSON常量参数说明：**

以下常量表示了 json_last_error() 所返回的错误类型。
~~~
JSON_ERROR_NONE (integer)
没有错误发生。自 PHP 5.3.0 起生效。

JSON_ERROR_DEPTH (integer)
到达了最大堆栈深度。自 PHP 5.3.0 起生效。

JSON_ERROR_STATE_MISMATCH (integer)
出现了下溢（underflow）或者模式不匹配。自 PHP 5.3.0 起生效。

JSON_ERROR_CTRL_CHAR (integer)
控制字符错误，可能是编码不对。自 PHP 5.3.0 起生效。

JSON_ERROR_SYNTAX (integer)
语法错误。 自 PHP 5.3.0 起生效。

JSON_ERROR_UTF8 (integer)
异常的 UTF-8 字符，也许是因为不正确的编码。 此常量自 PHP 5.3.1 起生效。
~~~


* * * * *

下面的常量可以和 json_encode() 的 form 选项结合使用。
~~~
JSON_HEX_TAG (integer)
所有的 < 和 > 转换成 \u003C 和 \u003E。 自 PHP 5.3.0 起生效。

JSON_HEX_AMP (integer)
所有的 & 转换成 \u0026。 自 PHP 5.3.0 起生效。

JSON_HEX_APOS (integer)
所有的 ' 转换成 \u0027。 自 PHP 5.3.0 起生效。

JSON_HEX_QUOT (integer)
所有的 " 转换成 \u0022。 自 PHP 5.3.0 起生效。

JSON_FORCE_OBJECT (integer)
使一个非关联数组输出一个类（Object）而非数组。 在数组为空而接受者需要一个类（Object）的时候尤其有用。 自 PHP 5.3.0 起生效。

JSON_NUMERIC_CHECK (integer)
将所有数字字符串编码成数字（numbers）。 自 PHP 5.3.3 起生效。

JSON_BIGINT_AS_STRING (integer)
将大数字编码成原始字符原来的值。 自 PHP 5.4.0 起生效。

JSON_PRETTY_PRINT (integer)
用空白字符格式化返回的数据。 自 PHP 5.4.0 起生效。

JSON_UNESCAPED_SLASHES (integer)
不要编码 /。 自 PHP 5.4.0 起生效。

JSON_UNESCAPED_UNICODE (integer)
以字面编码多字节 Unicode 字符（默认是编码成 \uXXXX）。 自 PHP 5.4.0 起生效。
~~~


* * * * *
