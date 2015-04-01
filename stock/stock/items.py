# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    stock_code = scrapy.Field()
    stock_name = scrapy.Field()
    stock_newest_price  = scrapy.Field()
    stock_ups_and_downs = scrapy.Field()
