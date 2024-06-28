# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy       
from scrapy import signals
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy_splash import SplashRequest, SplashJsonResponse  # Import both classes
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class NcarArchiveSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



    def process_request(self, request, spider):
        request.headers['Authorization'] = f'Bearer {self.auth_token}'
        return request

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.headers['Authorization'] = f'Bearer {self.auth_token}'
        return request
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        #return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


    def __init__(self, settings):
        super(MyCustomSplashMiddleware, self).__init__(settings)
        # You can access settings from your Scrapy settings file here

    def process_request(self, request, spider):
        url = request.url

        if "https://ncar.gov.sa/archive-guide/6" in url:
            # Add custom headers for URLs containing "category/"
            request.headers["X-My-Custom-Header"] = "Some value"
            request.headers["Another-Custom-Header"] = "Another Value"
        # Add custom meta data
        request.meta["custom_key1"] = "custom_value1"
        request.meta["custom_key2"] = {"nested": "value"}  # You can add nested data

        # You can also modify other request attributes like cookies or body

        return request

    def process_response(self, request, response, spider):
        # Modify the response object after receiving it from Splash
        # You might not need this logic if the sole purpose is adding headers and metadata

        return response



class RandomUserAgentMiddleware(object):

    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        """
        Scrapy calls this method to instantiate the middleware from crawler settings.
        """
        settings = crawler.settings
        user_agents = settings.get('USER_AGENTS')

        if not user_agents:
            raise NotConfigured("USER_AGENTS not defined in settings.py")

        return cls(user_agents)

    def process_request(self, request, spider):
        """
        This method intercepts outgoing requests and modifies them.
        """
        user_agent = random.choice(self.user_agents)
        request.headers.setdefault('User-Agent', user_agent)
        spider.logger.debug(f'Using User-Agent: {user_agent}')

class RandomUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        # Read user agent list from settings
        user_agent_list = crawler.settings.get('USER_AGENTS', [])
        return cls(user_agent_list)

    def process_request(self, request, spider):
        # Set random user agent from the list
        user_agent = random.choice(self.user_agent_list)
        request.headers.setdefault(b'User-Agent', user_agent.encode())


