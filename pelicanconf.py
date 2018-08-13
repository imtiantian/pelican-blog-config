#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AUTHOR = '天天'
SITENAME = '天天的博客'
#SITEURL = 'https://imtiantian.github.io'
#SITELOGO = 'pictures/logo.jpg'
FAVICON = 'pictures/favicon.ico'

PATH = 'content'
STATIC_PATHS = ['pictures','images', 'pdfs','static']#静态资源目录
SUMMARY_MAX_LENGTH = 20#设置文章摘要的长度
ARTICLE_URL = 'posts/{category}/{title}.html'
ARTICLE_SAVE_AS = 'posts/{category}/{title}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

DISPLAY_CATEGORIES_ON_MENU = False #是否在菜单上显示分类
DISPLAY_TAGS_ON_SIDEBAR = True#是否在侧边栏上显示标签
TAG_CLOUD_MAX_ITEMS = 100
DISPLAY_TAGS_INLINE=True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
# AVATAR='pictures/profile.jpg'
#ABOUT_ME='程序员'
# GITHUB_USER = 'imtiantian'
# GITHUB_SKIP_FORK = True
# GITHUB_SHOW_USER_LINK = True
HIDE_SIDEBAR=False

PYGMENTS_STYLE = 'monokai'#代码块样式：autumn，borland，bw，colorful，default，emacs，friendly，fruity，manni，monokai，murphy，native，pastie，perldoc，solarizeddark，solarizedlight，tango，trac，vim，vs，zenburn。默认为native
BOOTSTRAP_FLUID = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d（%a）'#时间格式
TIMEZONE = 'Asia/Shanghai'#时区

DEFAULT_LANG = 'Chinese (Simplified)'#语言

#TEMPLATE_PAGES = {'template_pages/*': 'template_pages/*'}

DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search','tags')

BANNER = 'pictures/banner.jpg'#索引页的横幅
BANNER_SUBTITLE = '自律给我自由'

DISPLAY_ARTICLE_INFO_ON_INDEX  = True#索引页显示文章日期，标签等信息
SHOW_ARTICLE_CATEGORY = True#文章页显示文章分类

#BOOTSTRAP_NAVBAR_INVERSE = True #bootstrap反向导航条
#For pelican-ootstrap3
BOOTSTRAP_THEME='journal'#simplex，yeti，superhero，cosmo，flatly，journal，readable，paper，cerulean


TAGS_URL = 'tags.html'

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

MARKDOWN = {
  'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
  },
  'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('文章','/'),
    ('标签', '/tags.html'),
    ('分类', '/categories.html'),
    ('归档','/archives.html')
)

# Blogroll
LINKS = (
    ('Django 1.8.2 中文文档', 'https://yiyibooks.cn/xx/django_182/index.html'),
    ('Python 3.5.2 中文文档','https://yiyibooks.cn/xx/python_352/index.html')
)



# Social widget
SOCIAL = (
    ('给我写信', 'http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=Uionfyg6OyU3PBIjI3wxPT8','envelope'),
)

DEFAULT_PAGINATION = 8

PLUGIN_PATHS = [os.path.join(BASE_DIR,'blog/pelican-plugins').replace('\\','/'), ]
PLUGINS = ['tipue_search','tag_cloud','i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

OUTPUT_PATH = os.path.join(BASE_DIR,'blog/output/').replace('\\','/')
THEME = os.path.join(BASE_DIR,'blog/pelican-themes/pelican-bootstrap3').replace('\\','/')



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
