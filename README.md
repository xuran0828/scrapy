这是几个练习scrapy项目的例子

scrapy shell 遇到404，403等的报错：
  有两种解决方法:

　　(1):第一种方法是在命令上加上-s USER_AGENT='Mozilla/5.0'

　　第一种方法最简单但是每次操作都要加上去很繁琐,第二种方法比较好。

　　(2):第二种方法是修改scrapy的user-agent默认值

　　找到python的:安装目录下的default_settings.py文件,比如我的C:\Users\0923\AppData\Local\Programs\Python\Python37\Lib\site-packages\scrapy\settings　　

　　把

　　　　USER_AGENT = 'Scrapy/%s (+http://scrapy.org)' % import_module('scrapy').__version__

　　改为

　　　　USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0'


　　使用shell再次，发现已经可以正常访问html不会在出现403错误了。
