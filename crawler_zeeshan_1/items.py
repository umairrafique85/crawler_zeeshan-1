# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class MercariZeeshanItem(Item):
    # Primary fields
    categorytitle = Field()
    brand = Field()
    itemsnames = Field()
    prices = Field()
    
    # Debug info fields
    url = Field()
    spider = Field()
    date = Field()
