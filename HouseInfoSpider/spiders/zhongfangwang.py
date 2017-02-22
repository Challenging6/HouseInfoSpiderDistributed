# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from ..items import HouseInfoItem

class ZFWSpider(RedisCrawlSpider):
    name = "zhongfangwang"
    allowed_domains = ["www.360fdc.com"]
    redis_key = "zhongfangwang:start_urls"

    #start_urls = (
    ##    'http://www.360fdc.com/ershoufang/',
   # )

    rules = (
       Rule(link_extractor=LinkExtractor(allow=('http://www.360fdc.com/ershoufang/[0-9]+\.html')), callback='parse_item',follow=True),
    )
    def parse_item(self, response):
        item = HouseInfoItem()
        try:
            bsObj = BeautifulSoup(response.body, 'lxml')
            item['url'] = response.url
            item['village_title'] = bsObj.find('div', class_='info1').h1.text.strip()			#标题
            item['village_total'] = bsObj.find('div', class_='rifleft').find('span').text.strip() 	#总价
            rowinfo_info = bsObj.find('div', class_='ps_r iright').findAll('div', class_='rowinfo_info')
            item['village_house_type'] = rowinfo_info[4].find('div', class_='rifright').text.strip()	#户型
            item['village_area'] = rowinfo_info[3].find('div', class_='rifright').text.strip()	#房子面积

            hoinf_text = bsObj.findAll('div', class_='Hoinf-text01')
            hoinf_text1 = hoinf_text[0].findAll('li')
            hoinf_text2 = hoinf_text[1].findAll('li')
            item['village_name'] =  hoinf_text2[0].span.a.text							#小区名
            item['village_location'] = hoinf_text2[2].span.text#小区位置
            item['village_age'] = hoinf_text1[1].span.text					#建造时间
            item['village_housing_type'] = hoinf_text1[4].span.text				#住宅类型
            item['village_direction'] = hoinf_text1[0].span.text		#朝向
            item['village_decoration'] = hoinf_text1[2].span.text				#装修类别
            item['village_floor'] = rowinfo_info[5].find('div', class_='rifright').text.strip()#楼层
            item['village_unit_price'] = bsObj.find('a', class_='stext').text.strip()		#单价
            item['village_down_payment'] = bsObj.find('div', id='couponText').find('span').text		#首付
            item['village_describe'] = bsObj.find('div', class_='Hoinf-div01 jinji').text.encode('utf-8').strip().replace('\n', '').replace('\r', '').replace('\t', '')	#描述
            item['village_monthly_payment'] = rowinfo_info[2].find('div', class_='rifright').text.strip()#月供

            jy = bsObj.find('div', class_='zbMapAll')
            item['lat'] = jy.get('data-lat')
            item['lng'] = jy.get('data-lon')
        except Exception as e:
            self.logger.error("parse url:%s err:%s",response.url,e)
        return item


