
# -*- coding: utf-8 -*-

# Scrapy settings for topgoods project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'topgoods'

SPIDER_MODULES = ['topgoods.spiders']
NEWSPIDER_MODULE = 'topgoods.spiders'

DEPTH_LIMIT = 2

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"


class USER_AGENT_ENUM(object):
    CHROME = 0
    FIREFOX = 1
    IE = 2
    ANDROID = 3
    IPHONE = 4


USER_AGENT_MAPPING = {
    USER_AGENT_ENUM.CHROME:
        'Mozilla/%s.0 (Windows NT %s.0; WOW%s) AppleWebKit/%s.36 (KHTML, like Gecko) Chrome/%s.0.2357.65 Safari/%s.36' \
        % (random.randint(4, 5), random.randint(8, 10), random.choice([32, 64]),
           random.randint(521, 537), random.randint(31, 43), random.randint(521, 537)),
    USER_AGENT_ENUM.FIREFOX:
        'Mozilla/%s.0 (Windows NT %s.0; WOW%s; rv:%s.0) Gecko/20100101 Firefox/%s.0' \
        % (random.randint(4, 5), random.randint(8, 10), random.choice([32, 64]), random.randint(29, 36),
           random.randint(29, 36)),
    USER_AGENT_ENUM.IE:
        'Mozilla/%s.0 (compatible; MSIE %s.0; Windows NT %s.1; WOW%s; Trident/%s.0)' \
        % (random.randint(4, 5), random.randint(8, 10), random.randint(8, 10), random.choice([32, 64]),
           random.randint(4, 5)),
    USER_AGENT_ENUM.ANDROID:
        'Mozilla/%s.0(Linux;U;Android4.%s.%s;zh-cn;%s)AppleWebKit/534.30(KHTML, likeGecko)Version/%s.0MobileSafari/534.30' \
        % (random.randint(4, 5), random.randint(0, 3), random.randint(0, 3), \
           random.choice(["nokia", "sony", "ericsson", "mot", "samsung", "sgh", "lg", "sie", "philips", "panasonic",
                          "alcatel", "lenovo", "cldc", "midp", "wap", "mobile"]), \
           random.randint(3, 5)),
    USER_AGENT_ENUM.IPHONE:
        'Mozilla/%s.0(iPhone;CPUiPhoneOS%s_%s_%slikeMacOSX)AppleWebKit/%s00.1.%s(KHTML, likeGecko)Mobile/12H321' \
        % (random.randint(4, 5), random.randint(6, 8), random.randint(0, 1), random.randint(0, 4),
           random.randint(4, 6), random.randint(1, 4))
}
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 4

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
}
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'topgoods.middlewares.ProxyMiddleware': 90,
    'topgoods.middlewares.RandomUserAgent': 490,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'topgoods.pipelines.TopgoodsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 3
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Mysql数据库的配置信息
MYSQL_HOST = '139.224.219.76'
MYSQL_DBNAME = 'testdb'  # 数据库名字，请修改
MYSQL_USER = 'root'  # 数据库账号，请修改
MYSQL_PASSWD = 'DavidZhang=123456'  # 数据库密码，请修改

MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

IPPOOL = None

# Output .csv
FEED_URI = u'goods.csv'
FEED_FORMAT = 'CSV'

HTTPERROR_ALLOWED_CODES = [302, ]