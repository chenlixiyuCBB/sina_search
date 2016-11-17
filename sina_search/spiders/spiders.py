# encoding=utf-8
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from sina_search.items import weiboItem
from scrapy.http import Request


class Spider(CrawlSpider):
    name = "sina_search"
    allowed_domains = ["http://weibo.cn"]
    page = 1
    urls = "http://weibo.cn/search/mblog?hideSearchFrame=&keyword=情话&page=%s" % page
    start_urls = [urls]

    def parse(self, response):
        weibos = Selector(response).xpath('//div[@class="c"]')
        if weibos is not None:
            for weibo in weibos:
                item = weiboItem()
                item['ID'] = weibo.xpath('@id').extract()
                item['Text'] = weibo.xpath('span[@class="ctt]/text()').extract()
                yield item
            self.page += 1
            yield Request(url=self.urls, meta={"item": weiboItem}, callback=self.parse)
        print "爬取完毕"
