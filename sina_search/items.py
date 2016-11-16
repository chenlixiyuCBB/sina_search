# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class weiboItem(Item):
    ID = Field()  # 微博ID
    Text = Field()  # 微博内容
