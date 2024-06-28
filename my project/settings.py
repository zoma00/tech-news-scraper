import os
os.environ['SCRAPY_LOG_LEVEL'] = 'DEBUG'


# Scrapy settings for MySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "my_spider"

SPIDER_MODULES = ["my_spider.spiders"]
NEWSPIDER_MODULE = "my_spider.spiders"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
]


DEFAULT_REQUEST_HEADERS = {
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Language': 'en',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
       'Accept-Encoding': 'gzip, deflate',
   }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "MyspiderResearchScraper/1.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = None
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
 # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
 #  "Accept-Language": "en",
#}


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
SPLASH_URL = 'http://192.168.16.209:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 724,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
   
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html

#CUSTOM_MIDDLEWARE{
  #  'my_spider.middleware.RandomUserAgentMiddleware': 500,
  #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#}



SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,  # Deduplicate Splash requests
    'scrapy_splash.SplashCookiesMiddleware': 300,  # Maintain cookie handling order
}



# Add the middleware to your settings
#CUSTOM_MIDDLEWARES = {
    #'my_spider.AddAuthHeaderMiddleware': 400,
#}

#DOWNLOADER_MIDDLEWARES = {
   # 'scrapy_splash.SplashCookiesMiddleware': 700,
   #  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
   #'scrapy_splash.SplashHeadersMiddleware': 760,
   #'scrapy_splash.SplashProxyMiddleware': 770,
   #'scrapy_proxy_pool.ProxyPoolMiddleware': 100,
   #'scrapy_proxy_pool.BanDetectionMiddleware': 600,
#}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_ENABLED = True

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "scrapy.extensions.telnet.TelnetConsole": True,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "my_spider.pipelines.My_spiderPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
#http://localhost:8050 not needed since using splash rquest and run it on this local host.
LOG_FILE = "my_spider_logs.txt"
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
