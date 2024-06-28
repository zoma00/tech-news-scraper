# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
import csv

class NcarArchivePipeline:

    def __init__(self):
        self.file_object = None

    def open_spider(self, spider):
        # Open CSV file in append mode (adjust path as needed)
        self.file_object = open('ncar_archives.csv', 'a', newline='')
        self.writer = csv.DictWriter(self.file_object, fieldnames=['dochrefs', 'titles', 'description'])
        # Write header row if file is empty
        if not self.file_object.tell():
            self.writer.writeheader()

    def close_spider(self, spider):
        # Close the CSV file
        self.file_object.close()

    def process_item(self, item, spider):
        # Write data to CSV
        self.writer.writerow(item)
        # You can optionally log the extracted data
        logger = spider.logger
        logger.info(f"Extracted data: {item}")
        return item
