# !/usr/bin/env 

import scrapy
from scrapy.loader import ItemLoader
from cvk.items import CvkItem


class BasicSpider(scrapy.Spider):
    """docstring for BasicSpider"""
    name = "basic"
    allowed_domains = ["web"]
    start_urls = [
        "http://www.cvk.gov.ua/pls/vm2015/PVM056?PID102="
        "2&PF7691=2&PT001F01=100&rej=0&pt00_t001f01=100"]

    def parse(self, response):
        """
        Initial parse
        """
        item_loader = ItemLoader(item=CvkItem(), response=response)
        item_loader.add_xpath(
            'name',
            '//table[@class="t2"][3]/tbody/tr/td[@class="td2"][2]/text()')
        item_loader.add_xpath(
            'birth',
            '//table[@class="t2"][3]/tbody/tr/td[@class="td2"][4]/text()')

        return item_loader.load_item()
