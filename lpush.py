#-*- coding: utf-8 -*-
import redis
try:
    r = redis.Redis(host='localhost', port=6379)
    r.lpush('anjuke:start_urls', 'http://wuhan.anjuke.com/sale/?from=navigation')
    r.lpush('zhongfangwang:start_urls', 'http://www.360fdc.com/ershoufang/')
    r.lpush('fangtianxia:start_urls', 'http://esf.wuhan.fang.com/chushou/3_159333352.htm')
    print "压入url成功!"
except Exception:
    print "压入失败"