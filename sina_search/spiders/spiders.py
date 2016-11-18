# encoding=utf-8
import re
from scrapy import Spider
from sina_search.items import weiboItem
from scrapy import Request
from bs4 import BeautifulSoup


class Spider(Spider):
    name = "sina_search"
    start_urls = ["http://weibo.cn/search/mblog?hideSearchFrame=&keyword=情话&page=1"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        pagelist = soup.find_all(id="pagelist")
        # 获取页数
        for pages in pagelist:
            pages = pages.get_text()

        pages = pages[pages.find('/') + 1: len(pages) - 1].encode('ascii')
        pages = int(pages)

        page = 0
        while page < pages:
            page += 1
            url = "http://weibo.cn/search/mblog?hideSearchFrame=&keyword=情话&page=" + str(page)
            yield Request(url, callback=self.parse_items)

    def parse_items(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        weibos = soup.find_all(id=re.compile("M_"))

        for weibo in weibos:
            if weibo.find("span", "ctt").get_text is not '':
                item = weiboItem()
                item['ID'] = weibo.find("a", "nk").get_text().encode("utf-8")
                item['Text'] = weibo.find("span", "ctt").get_text()[1:].encode("utf-8")
                yield item

