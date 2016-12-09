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

#https://ndb.nal.usda.gov/ndb/doc/apilist/API-NUTRIENT-REPORT.md
class NbdItem(Item):
	id = Field()
	weight = Field()
	measure = Field()
	caff_unit = Field()
	caff_value = Field()
	caff_gm = Field()
	pro_unit = Field()
	pro_value = Field()
	pro_gm = Field()
	fat_unit = Field()
	fat_value = Field()
	fat_gm = Field()
	carb_unit = Field()
	carb_value = Field()
	carb_gm = Field()
pass

#https://ndb.nal.usda.gov/ndb/doc/apilist/API-FOOD-REPORT.md
class FoodItem(Item):
	id = Field()
	name = Field()
	energy_unit = Field()
	energy_value = Field()
	pro_unit = Field()
	pro_value = Field()
	pro_gm = Field()
	fat_unit = Field()
	fat_value = Field()
	fat_gm = Field()
	carb_unit = Field()
	carb_value = Field()
	fiber_value = Field()
	fiber_unit = Field()
	sugar_unit = Field()
	sugar_value = Field()
pass