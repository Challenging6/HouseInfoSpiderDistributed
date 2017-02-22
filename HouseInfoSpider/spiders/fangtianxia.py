# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from ..items import HouseInfoItem
from address import AddressConvert

class FTXSpider(RedisCrawlSpider):
    name = "fangtianxia"
    allowed_domains = ["wuhan.fang.com"]
    redis_key = "fangtianxia:start_urls"
    #start_urls = (
    #    'http://esf.wuhan.fang.com/chushou/3_159333352.htm',
   # )

    rules = (
       Rule(link_extractor=LinkExtractor(allow=('http://esf.wuhan.fang.com/chushou/[0-9]_[0-9]*.htm')), callback='parse_item',follow=True),
    )
    def parse_item(self, response):
        item = HouseInfoItem()
        ac = AddressConvert()
        city = '武汉'
        try:
            bsObj = BeautifulSoup(response.body, 'lxml')
            item['url'] = response.url
            item['village_name'] =  bsObj.find('a', id='agantesfxq_B02_08').text		#小区名
            item['village_location'] = bsObj.find('div', id='esfwuhanxq_121').p.span.next_sibling+item['village_name']
            inforTxt1 =  bsObj.find('div', class_='inforTxt').findAll('dl')[0].findAll('dd')
            inforTxt2 =  bsObj.find('div', class_='inforTxt').findAll('dl')[1].findAll('dd')
            inforTxt3 = bsObj.find('div', class_='inforTxt').findAll('dl')[0].dt
            item['village_area'] = inforTxt1[3].span.text		#建筑面积
            item['village_age'] = inforTxt2[0].span.next_sibling.encode('utf-8')#房子年代
            item['village_direction'] = inforTxt2[1].span.next_sibling.encode('utf-8')#朝向
            item['village_decoration'] = inforTxt2[4].span.next_sibling.encode('utf-8')#装修程度
            item['village_floor'] = inforTxt2[2].span.next_sibling.encode('utf-8')#楼层
            item['village_house_type'] = inforTxt1[2].span.next_sibling.encode('utf-8')#户型
            item['village_unit_price'] = inforTxt3.find('span', class_='black').next_sibling.replace('(', '').replace(')', '').strip() #单价
            item['village_down_payment'] =  inforTxt1[0].span.next_sibling.text.encode('utf-8')			#首付			#首付
            item['village_housing_type'] = inforTxt2[5].span.next_sibling.encode('utf-8')
            item['village_total'] = inforTxt3.findAll('span')[1].text + inforTxt3.findAll('span')[2].text #总价
            item['village_title'] = bsObj.find('div', class_='title').h1.text.strip()       #标题
            item['village_describe'] = bsObj.find('div', class_='describe').text.replace('\n', '').strip()    #得到描述
            lat_lng = ac.locatebyAddr(item['village_location'], city)
            item['lat'] = lat_lng['lat']
            item['lng'] = lat_lng['lng']

        except Exception as e:
            self.logger.error("parse url:%s err:%s",response.url,e)
        return item


