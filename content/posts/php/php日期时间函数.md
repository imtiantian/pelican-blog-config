Title: php日期时间函数
Date: 2015-10-11 12:46
Tags: php



~~~
/**
* 生成从开始月份到结束月份的月份数组
* @param int $start 开始时间
* @param int $end 结束时间
*/
function monthList($start,$end){
	$month_arr = array();
	$start_timestamp = strtotime($start);
	$end_timestamp = strtotime($end);

	$start_timestamp = mktime(0, 0, 0, date("n", $start_timestamp), 1, date("Y", $start_timestamp));
	$next_timestamp = $start_timestamp;
	while ($next_timestamp <= $end_timestamp) {
	    $month_arr[] = date("Y-m", $next_timestamp);
	    $next_timestamp = mktime(0, 0, 0, date("n", $next_timestamp) + 1, date("j", $next_timestamp), date("Y", $next_timestamp));
	};
	return $month_arr;
}
~~~

* * * * *
~~~
	//得到日期的上个月的今天，如strtotime('2016-10-20')返回得到2016-09-20
	function last_month_today($time){
	    $last_month_time = mktime(date("G", $time), date("i", $time),
	                date("s", $time), date("n", $time), 0, date("Y", $time));
	    $last_month_t =  date("t", $last_month_time);
	    if ($last_month_t < date("j", $time)) {
	        return date("Ymt H:i:s", $last_month_time);
	    }
	    return date(date("Ym", $last_month_time) . "d", $time);
	}
~~~

* * * * *
~~~
	/*
	 * 根据两日期，获取之间的日期列表
	 * $start_time 开始日期 格式20160701
	 * $end_time 结束日期 格式20160916
	 * */
	function get_d_list($start_time,$end_time){
		$start_time = strtotime($start_time);
		$end_time = strtotime($end_time);
		$date_list = array();
		for($start_time;$start_time<=$end_time;$start_time=$start_time+3600*24){
			$date_list[] = date('Ymd',$start_time);
		}
		return $date_list;
	}
~~~

* * * * *
~~~
	/**
     * [显示友好的时间格式 xx分钟前  xx小时前  xx天 超过3天显示正常时间]
     * @param  [type] $date [description]
     * @return [type]       [description]
     */
    function dataStr($date){
        if((time()-$date)<60*10){
            //十分钟内
            echo '刚刚';
        }elseif(((time()-$date)<60*60)&&((time()-$date)>=60*10)){
            //超过十分钟少于1小时
            $s = floor((time()-$date)/60);
            echo  $s."分钟前";
        }elseif(((time()-$date)<60*60*24)&&((time()-$date)>=60*60)){
            //超过1小时少于24小时
            $s = floor((time()-$date)/60/60);
            echo  $s."小时前";
        }elseif(((time()-$date)<60*60*24*3)&&((time()-$date)>=60*60*24)){
            //超过1天少于3天内
            $s = floor((time()-$date)/60/60/24);
            echo $s."天前";
        }else{
            //超过3天
            echo  date("Y/m/d",$date);
        }

    }
~~~