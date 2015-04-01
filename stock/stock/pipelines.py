# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class StockPipeline(object):
    def process_item(self, item, spider):
    	def __init__(self):
		self.conn = MySQLdb.connect(host="localhost", db="mytest", user="root", passwd="", charset="utf8")
		self.curs = self.conn.cursor()
	def process_item(self, item, spider):
		self.curs.execute('INSERT INTO shenstock VALUES(%s, %s, %s, %s)', (item['stock_code'], item['stock_name'], item['stock_newest_price'], item['stock_ups_and_downs']))
		self.conn.commit()
		return item
