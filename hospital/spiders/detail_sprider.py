# -*- coding: utf-8 -*-

from hospital.items import DetailItem
from scrapy import *
import logging
from scrapy.utils.project import get_project_settings
import MySQLdb
import json

log = logging.getLogger('detail')

class detail_sprider(Spider):

    name='detail'
    #allowed_domains = ['baidu.com']


    def __init__(self, category=None, *args, **kwargs):
        super(detail_sprider, self).__init__(*args, **kwargs)
        settings = get_project_settings()
        ip=settings['MYSQL_IP']
        port= settings['MYSQL_PORT']
        db=settings['MYSQL_DB']
        user=settings['MYSQL_USER']
        passwd=settings['MYSQL_PWD']
        table=settings['PLACEID']
        conn=MySQLdb.connect(host=ip,user=user,passwd=passwd,db=db,charset="utf8")
        cursor=conn.cursor()
        carsql="SELECT place_id FROM placeid WHERE place_id !=%s"
        carparam=('---',)
        self.url_set1=set()
        cursor.execute(carsql,carparam)
        result=cursor.fetchall()
        for row in result:
            self.url_set1.add(row[0])
        print 'There are total ',
        print len(self.url_set1),
        print ' words in DB'

        existsql = "SELECT place_id FROM place_detail"
        #carparam = ('---',)
        self.url_set2 = set()
        cursor.execute(existsql)#, carparam)
        result = cursor.fetchall()
        for row in result:
            self.url_set2.add(row[0])
        print 'total ',

        self.url_set=self.url_set1-self.url_set2
        print len(self.url_set),
        print ' need to crawl'



        cursor.close()
        conn.close()


    def start_requests(self):
        settings = get_project_settings()
        key = settings['KEY9']
        request_list=[]
        for place_id in self.url_set:
            url='https://maps.googleapis.com/maps/api/place/details/json?key='+key+'&placeid='+place_id+'&language=en'
            request=Request(url,callback=self.parse)
            request_list.append(request)
        return request_list


    def parse(self, response):
        print '=======parse====='
        info = json.loads(response.body)
        status = info['status']
        if status not in ['OK']:
            print response.body
            raise Exception()



        item =DetailItem()
        data = info['result']
        formatted_address = data['formatted_address']
        lat = data['geometry']['location']['lat']
        lng = data['geometry']['location']['lng']
        international_phone_number = data.get('international_phone_number', '-')
        formatted_phone_number = data.get('formatted_phone_number', '-')
        name = data['name']
        rating = data.get('rating', '-')
        website = data.get('website', '-')
        url=data.get('url','-')

        item['place_id'] = data['place_id']
        item['vicinity'] = data['vicinity']
        item['formatted_address'] = formatted_address
        item['lat'] = str(lat)
        item['lng'] = str(lng)
        item['international_phone_number'] = str(international_phone_number)
        item['formatted_phone_number'] = str(formatted_phone_number)
        item['name'] = name
        item['rating'] = str(rating)
        item['website'] = website
        item['url'] = url

        yield item










