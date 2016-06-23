import scrapy
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException
from ScrapeGag.items import ScrapegagItem
 
logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)
 
 
class ScrapeGagSpider(scrapy.Spider):
	name = "getmegag"
	allowed_domains = ["9gag.com"]
	start_urls = [
		"http://www.9gag.com/"
	]
	
	def parse(self,response):
		item = ScrapeGagItem()
		driver = webdriver.Chrome()	
		driver.set_page_load_timeout(2)
		my_urls = []
		try:
			driver.get("http://www.9gag.com")
		except TimeoutException:
			logger.info('Handled!')
		if driver.find_elements_by_xpath('//div[@class="badge-entry-collection"]/article/div/a/img'):
			links = driver.find_elements_by_xpath('//div[@class="badge-entry-collection"]/article/div/a/img')
			for link in links:
				my_urls.append(link.get_attribute('src'))
		#my_urls = [u'http://img-9gag-fun.9cache.com/photo/aAPVwAo_460s.jpg', u'http://img-9gag-fun.9cache.com/photo/a7dKdyr_460s_v1.jpg' ...]
		if ...] driver.find_elements_by_xpath('//div[@class="loading"]/a'):
			pointer = driver.find_elements_by_xpath('//div[@class="loading"]/a')
			for url in pointer:
				next_url = url.get_attribute('href')
			#next url = http://9gag.com/?id=aZpWnV9%2CavnZPdd%2CaQxpV77&c=10 
			#For pagination, to be used later
		item['image_urls'] = ["https://s-media-cache-ak0.pinimg.com/564x/3a/a8/bd/3aa8bd1b9a1befe4fc77c1556e16a5f8.jpg"]	
		return item