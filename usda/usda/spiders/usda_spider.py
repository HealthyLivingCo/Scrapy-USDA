import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from datetime import date, time
import json
import datetime
import time
from usda.items import UsdaItem
from api_key import key

class USDASpider(Spider):
	name = "usda"
	start_urls = []
	
	def __init__(self):
		locations = (0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000,12500,13000,13500,14000,14500,15000,15500,16000,16500,17000,17500,18000,18500,19000,19500,20000,20500,21000,21500,22000,22500,23000,23500,24000,24500,25000,25500,26000,26500,27000,27500,28000,28500,29000,29500,30000,30500,31000,31500,32000,32500,33000,33500,34000,34500,35000,35500,36000,36500,37000,37500,38000,38500,39000,39500,40000,40500,41000,41500,42000,42500,43000,43500,44000,44500,45000,45500,46000,46500,47000,47500,48000,48500,49000,49500,50000,50500,51000,51500,52000,52500,53000,53500,54000,54500,55000,55500,56000,56500,57000,57500,58000,58500,59000,59500,60000,60500,61000,61500,62000,62500,63000,63500,64000,64500,65000,65500,66000,66500,67000,67500,68000,68500,69000,69500,70000,70500,71000,71500,72000,72500,73000,73500,74000,74500,75000,75500,76000,76500,77000,77500,78000,78500,79000,79500,80000,80500,81000)
		
		url_pattern = "http://api.nal.usda.gov/ndb/list?format=json&lt=f&sort=id&max=500&offset={offsetnum}&api_key={apikey}"
		
		for location in locations:
			self.start_urls.append(url_pattern.format(offsetnum=location, apikey=key))
			
	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		items = []
		for object in jsonresponse["list"]["item"]:
			item = UsdaItem()
			item["offset"] = object["offset"]
			item["id"] = object["id"]
			item["name"] = object["name"]
			items.append(item)
		return items