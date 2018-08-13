Title: 使用pelican搭建github pages博客
Date: 2017-10-19 11:20
Tags: python, pelican


打算将博客移到github上，比较过hexo,jekyll,pelican等静态博客生成工具，个人对于Python比较熟悉，于是选择了pelican.

### 安装
安装pelican
```
pip install pelican
```
安装可选包
```
如果您打算使用Markdown作为标记格式，则需要安装Markdown库：
pip install Markdown
可以在设置文件中启用排印增强功能，但首先必须安装必需的Typogrify库：
pip install typogrify
```

---

### 搭建博客站点
创建目录，存放pelican的框架
```
mkdir blog //创建文件夹
```
生成pelican的框架
```
pelican-quickstart//执行命令，生成pelican的框架
```

命令成功执行后，会出现pelican的框架，目录结构如下所示
```
blog/
├── content                # 存放输入的markdown或RST源文件
│   └── (pages)           # 存放手工创建的静态页面，可选
│   └── (posts)           # 存放手工创建的文章，可选
├── output                 # 存放最终生成的静态博客
├── develop_server.sh      # 测试服务器
├── Makefile               # 管理博客的Makefile
├── pelicanconf.py         # 配置文件
└── publishconf.py         # 发布文件，可删除
```
> 为了层次清楚，可以在`content`目录下新建`pages`和`posts`目录，分别存放单页面和文章

---

### 选择博客主题
在`blog`目录下，执行如下操作：

·克隆主题到本地
```
git clone https://github.com/getpelican/pelican-themes.git
```

·使用主题，在`pelicanconf.py`配置文件中，添加下面行
```
#这里根据自己喜好选择主题模板
THEME = 'pelican-themes/pelican-bootstrap3'
```

---

### 书写文章
在posts
```
Title: 测试文章
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, ceshi
Slug: ceshi
Authors: admin
Summary: Short version for index and feeds

测试文章内容.
```
上面个选项与其意义如下：

选项 | 意义
---|---
Title | 文章标题
Date | 发布时间
Modified|更新时间
Category|文章所属分类
Tags|文章标签
Slug|url名称
Authors|作者
Summary|简介

---

### 生成博客站点
```
pelican /path/to/your/content/ [-s path/to/your/settings.py]
```
如：在`blog`目录下执行`pelican content/`命令

---

### 预览生成的站点
在`output`目录下执行：
```
python -m http.server 9000
```
浏览 “http://localhost:9000/ ”地址预览效果

### `pelicanconf.py`配置文件详解
> 注：以下配置选项部分为`pelican`通用的配置选项，部分为`pelican-bootstrap3`模板独有的配置选项

选项 | 意义
---|---
AUTHOR | 默认作者
SITENAME | 网站名称
SITEURL|网站url
SITELOGO|网站logo
FAVICON|网站FAVICON
PATH|内容路径
STATIC_PATHS|静态资源目录
SUMMARY_MAX_LENGTH|文章摘要的长度
ARTICLE_URL|文章页url,例：'posts/{category}/{title}.html'
ARTICLE_SAVE_AS|生成的文章保存路径,例：'posts/{category}/{title}.html'
PAGE_URL|单页面url,'pages/{slug}.html'
PAGE_SAVE_AS|生成的单页面保存路径,'pages/{slug}.html'
DISPLAY_BREADCRUMBS|是否开启面包屑导航
DISPLAY_CATEGORY_IN_BREADCRUMBS|分类或单页面是否开启面包屑导航
DISPLAY_CATEGORIES_ON_MENU|是否在菜单上显示分类
DISPLAY_CATEGORIES_ON_SIDEBAR|是否在侧边栏上显示分类
DISPLAY_TAGS_ON_SIDEBAR|是否在侧边栏上显示标签
TAG_CLOUD_MAX_ITEMS|侧边栏显示标签的最大数量
DISPLAY_TAGS_INLINE|侧边栏标签样式是否内联
AVATAR|侧边栏用户头像
ABOUT_ME|侧边栏用户简介
GITHUB_USER|github用户名
GITHUB_SKIP_FORK|未知
GITHUB_SHOW_USER_LINK|是否展示github链接
HIDE_SIDEBAR|是否隐藏侧边栏
PYGMENTS_STYLE|代码块样式[^1]
BOOTSTRAP_FLUID|是否使用bootstrap流式布局
DEFAULT_DATE_FORMAT|文章时间格式
TIMEZONE|时区
DEFAULT_LANG|语言
DIRECT_TEMPLATES|内容集合索引页面,值为一个列表[^2]
BANNER|索引页的横幅图片
BANNER_SUBTITLE|横幅文字
DISPLAY_ARTICLE_INFO_ON_INDEX|索引页是否显示文章日期，标签等信息
SHOW_ARTICLE_CATEGORY|文章页是否显示文章分类
BOOTSTRAP_NAVBAR_INVERSE|是否为bootstrap反向导航条
BOOTSTRAP_THEME|bootstrap样式[^3]
TAGS_URL|标签页url
CUSTOM_CSS|自定义css样式文件路径
CUSTOM_JS|自定义js文件路径
MARKDOWN|markdown配置
MENUITEMS|额外菜单,如：`(('标签', '/tags.html'),)`
LINKS|链接，如：`(('我的博客', 'https://imtiantian.github.io'),)`
SOCIAL|如：(('给我写信', 'http://mail.qq.com/cgi-bin/**','envelope'),)
DEFAULT_PAGINATION|每页文章数量
PLUGIN_PATHS|插件路径
PLUGINS|使用的插件名称
JINJA_ENVIRONMENT|位置
OUTPUT_PATH|静态博客输出路径
THEME|使用的模板路径

---
### 文章详情页，添加内容导航

```
// 根据h1,h2,h3,h4标签，生成文章内容导航目录
function articleIndex() {
    var $article = $('#content>article>.entry-content');
    var $header = $article.find('h1, h2, h3,h4');
    if($header.length > 0){
        var _html = '<div class="panel panel-default widget-outline"><div class="panel-heading" id="hideOutline"><a data-toggle="collapse" href="#collapseDir">目录结构<span class="pull-right glyphicon glyphicon-chevron-down"></span></a></div><div id="collapseDir" class="panel-body panel-collapse collapse in"><ul id="articleIndex"></ul></div></div>';
        $('#sidebar').prepend(_html);
        var _tagLevel = 1;                  // 最初的level
        var _$wrap = $('#articleIndex');    // 最初的wrap
        $header.each(function(index) {
            if($(this).text().trim() === '') {     // 空的title
                return;
            }
            //$(this).attr('id', 'articleHeader' + index);      // 加id
            //var this_id = 'articleHeader' + index;
            var this_id = $(this).attr('id');
            var _tl = parseInt($(this)[0].tagName.slice(1));  // 当前的tagLevel
            var _$li = null;
            if(index === 0 || _tl === _tagLevel) {  // 第一个或者是与上一个相同
                _$li = $('<li><a href="#'+ this_id +'">' + $(this).text() + '</a></li>');
                _$wrap.append(_$li);
            } else if(_tl > _tagLevel) {  // 当前的大于上次的
                _$li = $('<ul><li><a href="#' + this_id + '">' + $(this).text() + '</a></li></ul>');
                _$wrap.append(_$li);
                _$wrap = _$li;
            } else if(_tl < _tagLevel) {    // 当前的小于上次的
                _$li = $('<li><a href="#' + this_id + '">' + $(this).text() + '</a></li>');
                if(_tl === 1) {
                    $('#articleIndex').append(_$li);
                    _$wrap = $('#articleIndex');
                } else {
                    _$wrap.parent('ul').append(_$li);
                    _$wrap = _$wrap.parent('ul');
                }
            }
            _tagLevel = _tl;
        });
    }
}
```
---

[^1]: 代码块样式选项：autumn，borland，bw，colorful，default，emacs，friendly，fruity，manni，monokai，murphy，native，pastie，perldoc，solarizeddark，solarizedlight，tango，trac，vim，vs，zenburn。默认为native

[^2]: 内容集合索引：index，categories，authors，archives

[^3]: bootstrap样式选项:simplex，yeti，superhero，cosmo，flatly，journal，readable，paper，cerulean



