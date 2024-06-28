import scrapy
import csv

from scrapy.crawler import CrawlerProcess


class GetInfoSpider(scrapy.Spider):
    name = "get_info_spider"
    # ... define your spider logic here (start_requests, parse, etc.)

# Create a CrawlerProcess object
process = CrawlerProcess()

# Crawl the GetInfoSpider
process.crawl(GetInfoSpider)

# Start the crawl process
process.start()
