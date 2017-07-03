# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlaceIdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    place_id= scrapy.Field()
    description= scrapy.Field()
    input = scrapy.Field()
    country = scrapy.Field()
    location = scrapy.Field()
    status= scrapy.Field()
    place_id_count= scrapy.Field()


class DetailItem(scrapy.Item):
    place_id = scrapy.Field()
    vicinity= scrapy.Field()
    formatted_address= scrapy.Field()
    lat= scrapy.Field()
    lng= scrapy.Field()
    international_phone_number= scrapy.Field()
    formatted_phone_number= scrapy.Field()
    name= scrapy.Field()
    rating= scrapy.Field()
    website= scrapy.Field()
    url=scrapy.Field()

