# encoding=utf-8
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from sina_search.items import weiboItem


class Spider(CrawlSpider):
    name = "sina_search"
    host = "http://weibo.cn"
    page = 1
    urls = "http://weibo.cn/search/mblog?hideSearchFrame=&keyword=情话&page=%s" %page
    start_urls = [urls]
    scrawl_ID = set(start_urls)  # 记录待爬的微博ID
    finish_ID = set()  # 记录已爬的微博ID


    def parse(self, response):
      weibos = Selector(response).xpath('//div[@class="c"]')

      for  weibo in weibos:
          item = weiboItem()
          item['ID'] = weibo.xpath('@id').extract()
          item['Text'] = weibo.xpath('span[@class="ctt]/text()').extract()
          yield item
