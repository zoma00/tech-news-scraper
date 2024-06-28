import scrapy


class My_spider(scrapy.Item):
    dochrefs = scrapy.Field()  # Field to store links (URLs)


class MySpider(scrapy.Spider):
    name = 'ncar_spider'  # Unique name for your spider
    start_urls = ['https://ncar.gov.sa/archive-guide/6']  # Starting URL for crawl

    def parse(self, response):
        # Target the specific anchor tag using the provided selector
        archive_items = response.css('body > app-root > app-guide > div > div > div.container > div:nth-child(1) > a')

        for archive_item in archive_items:
            # Extract href from the 'href' attribute of the anchor tag
            href = archive_item.css('::attr(href)').get()

            # Find the span element with the title (assuming it's the only one)
            title_span = archive_item.css('div > div.d-flex.bd-highlight > div > span.card-title')

            

            # Create a new NcarArchiveItem instance and populate it
            item = MyspiderItem()
            item['dochrefs'] = href

            # Yield the populated item
            yield item
