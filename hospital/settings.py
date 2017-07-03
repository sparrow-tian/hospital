# -*- coding: utf-8 -*-

# Scrapy settings for hospital project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hospital'

SPIDER_MODULES = ['hospital.spiders']
NEWSPIDER_MODULE = 'hospital.spiders'


DOWNLOAD_TIMEOUT = 300

MYSQL_IP='127.0.0.1'
MYSQL_PORT=3306
MYSQL_DB='test'
MYSQL_USER='root'
MYSQL_PWD=''
PLACEID='placeid'
DETAIL='place_detail'
KEY2='AIzaSyCdbANZZ5X-1Uf5MyT7qhndyRZFCA1BL6Q'
KEY3='AIzaSyBsp1YIX2ZDVgC2ijrfGylYv3CAgj66FbY'
KEY4='AIzaSyDj4ii1KU8DYfo-iX2tZ8qHZ809HJFBDJg'
KEY5='AIzaSyBrtHOE1_nmtkxmxWh5gEEM4pHMLfs0Bew'
KEY7='AIzaSyCLdwRrg2rPDjy5rXaWUHZFa0aiulnDN70'
#15000
KEY1='AIzaSyA9dojJ0Y9AHElwgg_duCAA_resZlLKs-Q'
KEY6='AIzaSyBcadJKlpRNL5ksgO4PbslHIzlWsD59oKo'
KEY8='AIzaSyChEwGxVCQgdWo6o7g-u2CsZZCSdSNWDJY'
KEYXQG='AIzaSyD7WN9_cviluafL87l4BuhivjICOF8eJLU'
KEY9='AIzaSyBN3mTFcBkpfAMgT0Tx43cspgNVua3n6sg'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hospital (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hospital.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
##DOWNLOADER_MIDDLEWARES = {
#    'hospital.myproxy.ProxyMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hospital.pipemysql.SQLStorePipeline': 300,
    #'hospital.pipelines.WebcrawlerScrapyPipeline': 300,#保存到mysql数据库
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
