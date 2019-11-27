# -*- coding: utf-8 -*-

# Scrapy settings for hosp_crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hosp_crawl'

SPIDER_MODULES = ['hosp_crawl.spiders']
NEWSPIDER_MODULE = 'hosp_crawl.spiders'

MYSQL_DB_NAME='dspdb_hsp_crawl'
MYSQL_HOST='10.10.172.148'
MYSQL_PORT=3306
MYSQL_USER='ranxu'
MYSQL_PASSWORD='Ran_Xu2019'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hosp_crawl (+http://www.yourdomain.com)'
PROXY_URL = 'http://localhost:5555/random'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'kztoken=nJail6zJp6iXaJqWl3BlYGFwaZaV; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZZOW%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZZyU%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpSZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpya%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5OT%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5mY%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJSS%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJWU%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJiY%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaZaV%22%3B%7D; acw_tc=707c9f9415730082259622365e4f58ea115862da5acc46bff21259d9f0c8ef; think_language=zh-CN; PHPSESSID=lrar70jh1ig5gt3jpsj6lne304; hmap_show=true; _ga=GA1.2.1853614770.1573008278; _gid=GA1.2.10628983.1573008278; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1573008278; linchuangshiyan_show=true; kztoken=nJail6zJp6iXaJqWl3BlYGFwaZiS; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZZyU%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpSZ%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpya%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5OT%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5mY%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJSS%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJWU%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJiY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaZaV%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaZiS%22%3B%7D; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1573008898',
    'Host': 'db.yaozh.com',
    'Referer': 'https://db.yaozh.com/hmap',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hosp_crawl.middlewares.HospCrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'hosp_crawl.middlewares.ProxyMiddleware': 300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hosp_crawl.items.HospCrawlItem':350,
   'hosp_crawl.pipelines.MySQLPipeline': 400,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
