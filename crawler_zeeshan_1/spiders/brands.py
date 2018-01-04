# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import socket
from scrapy.http import Request
from crawler_zeeshan_1.items import MercariZeeshanItem
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BrandsSpider(CrawlSpider):
    name = 'brands'
    allowed_domains = ['www.mercari.com']
    start_urls = ['https://www.mercari.com/brand/7255/?page=1']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="pagination-cell pager-cell visible-pc" and position() = (last()-1)]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        l = ItemLoader(item=MercariZeeshanItem(), response=response)

        l.add_xpath('brand', '//h3[contains(@class, "page-title title3")]/text()', MapCompose(str.strip, str.title))
        l.add_xpath('itemsnames', '//h3[@class="items-box-name font-3"]/text()')
        l.add_xpath('prices', '//div[@class="items-box-price font-6"]/text()', re='[,.0-9]+')

        return l.load_item()
