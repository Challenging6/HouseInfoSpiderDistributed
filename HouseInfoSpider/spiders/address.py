# coding:utf-8
import requests
import json
import re


class AddressConvert(object):
    def __init__(self):
        self.flag = 1
        self.ak = ['N6ylwnEcF1UNXoek5ITEvRUNZz2C9YGE', 'kmgAFIco6RqA4RVzoCX53YxpVz0d65N9']

    # 匹配地址
    def searchByScript(self, scripts):
        texts = str()
        for i in scripts:
            s = str(i)
            texts += s
        model = re.compile(r'[0-9]+\.[0-9]+')  # 匹配地址
        lat = float(re.findall(model, str(re.findall(r"lat=[0-9]+\.[0-9]+", texts)))[0])
        lng = float(re.findall(model, str(re.findall(r"lng=[0-9]+\.[0-9]+", texts)))[0])
        return lat, lng

    def locatebyAddr(self, address, city=None):
        items = {'output': 'json', 'ak': self.ak[self.flag], 'address': address}
        if city:
            items['city'] = city
        r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
        status = re.findall("\d+", r.content)[0]
        if status == "302":
            self.flag = (1 if self.flag == 0 else 0)
            items['ak'] = self.ak[self.flag]
            r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
        dictResult = json.loads(r.text)
        return dictResult['result']['location'] if not dictResult['status'] else None

    def locatebyLatLon(self, lat, lon, pois=0):
        items = {'location': str(lat) + ',' + str(lon), 'ak': 'kmgAFIco6RqA4RVzoCX53YxpVz0d65N9', 'output': 'json'}
        if pois:
            items['pois'] = 1
        r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
        status = re.findall("\d+", r.content)[0]
        if status == "302":
            self.flag = (1 if self.flag == 0 else 0)
            items['ak'] = self.ak[self.flag]
            r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
        dictResult = json.loads(r.text)
        return dictResult['result'] if not dictResult['status'] else None
