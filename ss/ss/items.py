# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class multivan(scrapy.Item):
    sludinajums = scrapy.Field()
    gads = scrapy.Field()
    tilp = scrapy.Field()
    nobraukums = scrapy.Field()
    cena = scrapy.Field()
    apskate = scrapy.Field()
    url = scrapy.Field()
    aprikojums = scrapy.Field()
    datums = scrapy.Field()

class scooters(scrapy.Item):
    sludinajums = scrapy.Field()
    marka = scrapy.Field()
    gads = scrapy.Field()
    stavoklis = scrapy.Field()
    cena = scrapy.Field()
    datums = scrapy.Field()
    url = scrapy.Field()
