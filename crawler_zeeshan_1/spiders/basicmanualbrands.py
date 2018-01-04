# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import socket
import datetime
from scrapy.http import Request
from crawler_zeeshan_1.items import MercariZeeshanItem
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader

class BasicmanualbrandsSpider(scrapy.Spider):
    name = 'basicmanualbrands'
    allowed_domains = ['www.mercari.com']
    start_urls = ['https://www.mercari.com/brand/7255/']

    def parse(self, response):
#        itemgroup_selector = response.xpath('//a[contains(@class, "brand-group-link-box-link-name white text-center")]/@href')
#        for url in itemgroup_selector.extract():
#            brand_selector = response.xpath('//div[contains(@class, "brand-list-initial-box-brand-list clearfix")]/a/@href')
#            for url in brand_selector:
#                yield Request(urllib.parse.urljoin(response.url, url), callback=self.parse_item)
        next_selector = response.xpath('//div[@class="pagination-cell pager-cell visible-pc" and position() = (last()-1)]/a/@href')
        for url in next_selector.extract():
            yield Request(urllib.parse.urljoin(response.url, url), callback=self.parse_item)
        
        
    def parse_item(self, response):
        l = ItemLoader(item=MercariZeeshanItem(), response=response)

        l.add_xpath('brand', '//h3[contains(@class, "page-title title3")]/text()', MapCompose(str.strip, str.title))
        l.add_xpath('itemsnames', '//h3[@class="items-box-name font-3"]/text()')
        l.add_xpath('prices', '//div[@class="items-box-price font-6"]/text()', re='[,.0-9]+')

        return l.load_item()
