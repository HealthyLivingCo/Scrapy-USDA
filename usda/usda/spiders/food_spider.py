import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from datetime import date, time
import json
import datetime
import time
from usda.items import FoodItem
from all_foods import big_array
from api_key import key

class FoodSpider(Spider):
	name = "food"

	start_urls = []
	
	def __init__(self):
		locations = big_array
		
		url_pattern = "http://api.nal.usda.gov/ndb/reports/?ndbno={offsetnum}&type=f&format=json&api_key={apikey}"
		
		for location in locations:
			self.start_urls.append(url_pattern.format(offsetnum=location, apikey=key))
			
		#Documentation for this API
		##https://ndb.nal.usda.gov/ndb/doc/apilist/API-FOOD-REPORT.md
			
	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		items = []
		item = FoodItem()
		item["id"] = jsonresponse["report"]["food"]["ndbno"]
		item["name"] = jsonresponse["report"]["food"]["name"]
		item["energy_unit"] = jsonresponse["report"]["food"]["nutrients"][0]["unit"]
		item["energy_value"] = jsonresponse["report"]["food"]["nutrients"][0]["value"]
		item["pro_value"] = jsonresponse["report"]["food"]["nutrients"][1]["value"]
		item["pro_unit"] = jsonresponse["report"]["food"]["nutrients"][1]["unit"]
		item["fat_value"] = jsonresponse["report"]["food"]["nutrients"][2]["value"]
		item["fat_unit"] = jsonresponse["report"]["food"]["nutrients"][2]["unit"]
		item["carb_value"] = jsonresponse["report"]["food"]["nutrients"][3]["value"]
		item["carb_unit"] = jsonresponse["report"]["food"]["nutrients"][3]["unit"]
		item["fiber_value"] = jsonresponse["report"]["food"]["nutrients"][4]["value"]
		item["fiber_unit"] = jsonresponse["report"]["food"]["nutrients"][4]["unit"]
		item["sugar_value"] = jsonresponse["report"]["food"]["nutrients"][5]["value"]
		item["sugar_unit"] = jsonresponse["report"]["food"]["nutrients"][5]["unit"]
		items.append(item)
		return items