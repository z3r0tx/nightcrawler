import scrapy
import re


class CnnTechSpider(scrapy.Spider):
    name = 'cnn_tech'
    start_urls = ['https://www.cnn.com/business/tech']

    def parse(self, response, **kwargs):
        for headlines in response.css('a.container__link'):
            title = headlines.css('span.container__headline-text::text').get()
            href = headlines.css('a.container__link').attrib['href']

            # Use regular expressions to extract the date from the URL
            date_match = re.search(r'/(\d{4}/\d{2}/\d{2})/', href)

            if title and href is not None and date_match:
                # Extract the date and format it as YYYY-MM-DD
                date = date_match.group(1).replace('/', '-')
                link = f"https://cnn.com{href}"

                yield {
                    'title': title,
                    'link': link,
                    'publication_date': date
                }
