import re
from datetime import datetime

import scrapy


class AbcNewsSpider(scrapy.Spider):
    name = "abc_news"
    start_urls = ["https://abcnews.go.com/xmlLatestStories"]
    current_datetime = datetime.now()

    def parse(self, response, **kwargs):
        xml_content = response.text

        loc_pattern = r'<loc>(.*?)<\/loc>'
        date_pattern = r'<news:publication_date>(.*?)<\/news:publication_date>'
        title_pattern = r'<news:title>(.*?)<\/news:title>'

        loc_matches = re.findall(loc_pattern, xml_content, re.DOTALL)
        date_matches = re.findall(date_pattern, xml_content, re.DOTALL)
        title_matches = re.findall(title_pattern, xml_content, re.DOTALL)

        for loc, date, title in zip(loc_matches, date_matches, title_matches):
            yield {
                'source_id': 1,
                'title': title.strip(),
                'link': loc.strip(),
                'publication_date': date.strip(),
                'visited_on': self.current_datetime
            }
