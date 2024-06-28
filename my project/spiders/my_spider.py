import scrapy
from scrapy_splash import SplashRequest, SplashJsonResponse  # Import both classes

from scrapy.selector import Selector
from logging import getLogger
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess

import logging
import scrapy

from scrapy.spiders import Spider
from scrapy.utils.request import request_fingerprint  # Deprecated

#from scrapy.exceptions import SplashRequestError

class NcarArchiveSpider(Spider):
    name = 'ncar_spider'
    allowed_domains = ['talabat.com']
    start_urls = ['https://www.talabat.com/egypt/elbatal']  # Replace with actual starting URL

    def __init__(self):
       def __init__(self):
        super(NcarArchiveSpider, self).__init__()
        self.logger = logging.getLogger(__name__)  # Initialize logger

    def parse(self, response):
        self.logger.info(f"Full Response Text (for debugging):\n {response.text[:100]}...")  # Truncate for readability

        # Check for JavaScript content (optional)
        if response.headers.get('Content-Type', '').lower() == 'application/javascript':
            self.logger.info(f"Received JavaScript content for URL: {response.url}")
            # Implement logic for handling JavaScript content (optional)
            # ... (e.g., return or handle differently)

        # Process response based on Splash or non-Splash type
        if isinstance(response, SplashJsonResponse):
            archive_items = response.data.get("archive_items", [])  # Access data from Lua script (if provided)
            self.logger.info(f"Extracted {len(archive_items)} archive items from Lua script.")
        else:
            self.logger.warning(f"Received non-Splash response for URL: {response.url}")
            archive_items = response.css("div.container a.card-title")  # Replace with your actual selector

        # Iterate through archive items
        data_list = []
        for item in archive_items:
            try:
                dochref = item.css("a.card-title::attr(href)").get()
                title = item.xpath(".//h6/span/text()").get()
                description = item.xpath(".//div[@class='card-result-card']//text()").getall()  # Get a list for multi-line descriptions
                description = " ".join(description).strip()  # Join and strip whitespace for a single string
                if not dochref or len(dochref) < 5:  # Check for minimum URL length
                    self.logger.warning(f"Invalid dochref found: {dochref}")
                    continue

                # Check for missing data within the loop (optional)
                if not all([dochref, title, description]):
                    self.logger.debug(f"Potential issue with selectors for item: {item}")
                    continue  # Skip item to avoid empty data

                data_dict = {
                    "dochrefs": dochref,
                    "titles": title,
                    "descriptions": description,
                }
                data_list.append(data_dict)
            except (AttributeError, TypeError) as e:
                self.logger.error(f"Missing attribute while extracting data: {e}")
            except TypeError as e:
                self.logger.error(f"Type error during data extraction: {e}")
            except SplashRequestError as e:
                self.logger.error(f"Error making Splash request: {e}")
            if response.status != 200:
                self.logger.error(f"Error: Unexpected status code {response.status} for URL: {response.url}")
                # Optionally, return or handle the error differently

        # Follow next page (optional)
        next_page_url = response.css('a.next-page::attr(href)').get()
        if next_page_url:
            yield SplashRequest(next_page_url, callback=self.parse)

        yield data_list  # Yield scraped data items



    def write_to_csv(self, item):
        filepath = "C:/Users/Hazem EL-Batawy/OneDrive/Desktop/ncar_archive/ncar_archives.csv"  # Adjust path as needed
        print(f"Saving data to: {filepath}")

        with open(filepath, "a", newline="") as csvfile:
            fieldnames = [
                "dochrefs",
                "titles",
                "description",
            ]  # Adjust fieldnames as needed
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write header row only if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(item)


# Run the spider using Scrapy
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(NcarSpider)
    process.start()


