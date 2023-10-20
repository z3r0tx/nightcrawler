# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NightCrawlerPipeline:
    def process_item(self, item, spider):
        return item

# import psycopg2
# from scrapy import Item
#
#
# class PostgresPipeline:
#     def __init__(self, settings):
#         self.settings = settings
#         self.conn = None
#         self.cur = None
#
#     @classmethod
#     def from_crawler(cls, crawler, *args, **kwargs):
#         settings = crawler.settings
#         return cls(settings)
#
#     def open_spider(self, spider):
#         self.conn = psycopg2.connect(**self.settings['DATABASE_SETTINGS'])
#         self.cur = self.conn.cursor()
#
#     def close_spider(self, spider):
#         if self.cur:
#             self.cur.close()
#         if self.conn:
#             self.conn.commit()
#             self.conn.close()
#
#     def process_item(self, item, spider):
#         if isinstance(item, Item):
#             sql = "INSERT INTO news_data (source_id, title, link, publication_date, visited_on) VALUES (%s, %s, %s, %s, %s)"
#             values = (item['source_id'], item['title'], item['link'], item['publication_date'], item['visited_on'])
#             self.cur.execute(sql, values)
#         return item
