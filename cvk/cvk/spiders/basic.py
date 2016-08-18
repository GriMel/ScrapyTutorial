# !/usr/bin/env 

import scrapy
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
        item = CvkItem()
        item['name'] = response.xpath(
            '//table[@class="t2"][3]/tbody/tr/td[@class="td2"][2]/text()').extract()
        item['birth'] = response.xpath(
            '//table[@class="t2"][3]/tbody/tr/td[@class="td2"][4]/text()').extract()
        return item
