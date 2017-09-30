import scrapy

class firstSpider(scrapy.Spider):
        name = "FTO_spider"
        start_urls = ['https://www.state.gov/j/ct/rls/other/des/123085.htm']

