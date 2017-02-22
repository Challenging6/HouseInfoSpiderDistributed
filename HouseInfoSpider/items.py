# -*- coding: utf-8 -*-

import scrapy

class HouseinfospiderItem(scrapy.Item):
    pass

class HouseInfoItem(scrapy.Item):
    url = scrapy.Field()                    #当前网页的url
    lat = scrapy.Field()                    #经度
    lng = scrapy.Field()                    #维度
    village_name = scrapy.Field()           #小区名
    village_location = scrapy.Field()       #小区位置
    village_area = scrapy.Field()           #房屋面积
    village_age = scrapy.Field()            #建造时间
    village_direction = scrapy.Field()      #朝向
    village_decoration = scrapy.Field()     #装修程度
    village_floor = scrapy.Field()          #楼层
    village_house_type = scrapy.Field()     #户型
    village_unit_price = scrapy.Field()     #单价
    village_down_payment = scrapy.Field()   #首付
    village_housing_type = scrapy.Field()   #住宅类型
    village_total = scrapy.Field()          #总价
    village_title = scrapy.Field()          #标题
    village_describe = scrapy.Field()       #描述
    village_monthly_payment = scrapy.Field()#月供