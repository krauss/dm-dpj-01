import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    start_urls = [
        'https://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/',
    ]

    def parse(self, response):
        for proxy_entry in response.css('tr.Odd'):
            yield {
                'entry': proxy_entry.css('td::text').getall()
            }

        #next_page = response.css('li.next a::attr("href")').get()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)