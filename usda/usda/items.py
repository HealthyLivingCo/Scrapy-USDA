# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class UsdaItem(Item):
    id = Field()
    name = Field()
    offset = Field()
pass