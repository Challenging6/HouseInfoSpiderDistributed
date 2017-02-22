# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from ..items import HouseInfoItem
from address import AddressConvert

class AJKSpider(RedisCrawlSpider):
    name = "anjuke"
    allowed_domains = ["wuhan.anjuke.com"]
    redis_key = "anjuke:start_urls"
    #start_urls = (
    #    'http://wuhan.anjuke.com/sale/?from=navigation',
    #)

    rules = (
       Rule(link_extractor=LinkExtractor(allow=('http://wuhan.anjuke.com/prop/view/A[0-9]+')), callback='parse_item',follow=True),
    )
    def parse_item(self, response):
        item = HouseInfoItem()
        ac = AddressConvert()
        city = "武汉"
        try:
            bsObj = BeautifulSoup(response.body, 'lxml')
            item['url'] = response.url
            item['village_title'] = bsObj.find('h3', class_='long-title').text.strip()			#标题
            item['village_total'] = bsObj.find('span', class_='light info-tag').text.strip()	#总价
            item['village_house_type'] = bsObj.find('span', class_='info-tag').text	.strip()	#户型
            item['village_area'] = bsObj.find('span', class_='info-tag no-border').text.strip()	#房子面积
            house_info1 = bsObj.find('div', class_='first-col detail-col').findAll('dl')
            house_info2 = bsObj.find('div', class_='second-col detail-col').findAll('dl')
            house_info3 = bsObj.find('div', class_='third-col detail-col').findAll('dl')
            item['village_name'] =  house_info1[0].dd.a.text.strip()							#小区名
            item['village_location'] = house_info1[1].dd.p.text.replace(u'\uff0d', '').replace('\t', '').replace('\n', '').replace(' ', '')																		  #小区位置
            item['village_age'] = house_info1[2].dd.text										#建造时间
            item['village_housing_type'] = house_info1[3].dd.text								#住宅类型
            item['village_direction'] = house_info2[2].dd.text									#朝向
            item['village_floor'] = house_info2[3].dd.text.replace('\t', '')									#楼层
            item['village_decoration'] = house_info3[0].dd.text									#装修程度
            item['village_unit_price'] = house_info3[1].dd.text.encode('utf-8')					#单价
            item['village_down_payment'] = house_info3[2].dd.contents[0].strip()				#首付
            item['village_describe'] = bsObj.find('div', class_='desc-article').text.strip()	#描述
            item['lat'], item['lng'] = ac.searchByScript(bsObj.body.findAll('script'))

        except Exception as e:
            self.logger.error("parse url:%s err:%s",response.url,e)
        return item


