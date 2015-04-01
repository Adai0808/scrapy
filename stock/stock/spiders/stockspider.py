# -*- coding: utf-8 -*-

from scrapy      import Spider
from stock.items import StockItem
from scrapy.http import Request

class StockSpider(Spider):
    name            = "stock"
    allowed_domains = ["http://app.finance.ifeng.com/list/stock.php?"]
    start_urls      = []
    for i in range(1, 20):
    	start_urls.append("http://app.finance.ifeng.com/list/stock.php?t=sa&f=symbol&o=asc&p=%d"%i)	

    def parse(self, response):
        links = response.xpath('//div[@class="tab01"]/table/tr[position()>1]')
        for link in links:
			code = link.xpath('td[1]/a[@target="_blank"]/text()').extract()
			name = link.xpath('td[2]/a[@target="_blank"]/text()').extract()
			newest_price  = link.xpath('td[3]/span[@class="Ared"]/text()').extract()
			ups_and_downs = link.xpath('td[4]/span[@class="Ared"]/text()').extract()

			item = StockItem()
			item['stock_code'] = code
			item['stock_name'] = name
			item['stock_newest_price']  = newest_price
			item['stock_ups_and_downs'] = ups_and_downs
			yield item
