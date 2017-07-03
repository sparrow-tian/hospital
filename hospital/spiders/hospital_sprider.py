# -*- coding: utf-8 -*-

from hospital.items import PlaceIdItem
from scrapy import *
import logging
from scrapy.utils.project import get_project_settings
import MySQLdb
import json
import lxml.etree as etree
import re
log = logging.getLogger('hospital')

class hospital_sprider(Spider):

    name='placeids'
    #allowed_domains = ['baidu.com']


    def __init__(self, category=None, *args, **kwargs):
        super(hospital_sprider, self).__init__(*args, **kwargs)
        settings = get_project_settings()
        ip=settings['MYSQL_IP']
        port= settings['MYSQL_PORT']
        db=settings['MYSQL_DB']
        user=settings['MYSQL_USER']
        passwd=settings['MYSQL_PWD']
        table=settings['PLACEID']
        conn=MySQLdb.connect(host=ip,user=user,passwd=passwd,db=db,charset="utf8")
        #conn=MySQLdb.connect(host=ip,user=user,db=db,charset="utf8")
        cursor=conn.cursor()
        #carsql="SELECT input FROM placeid where country=%s"
        carsql="SELECT input FROM placeid"
        carparam=('th',)
        self.url_set=set()
        cursor.execute(carsql)
        result=cursor.fetchall()
        for row in result:
            self.url_set.add(row[0])
        print 'There are total ',
        print len(self.url_set),
        print ' words in DB'
        cursor.close()
        conn.close()


    def start_requests(self):

        request_list = []
        with open('input/th2.txt','r') as rf:
            for line in rf:
                if line.strip()!="":
                    input = line.split('----->')[0].strip()
                    location = line.split('----->')[1].strip()
                    country=line.split('----->')[2].strip()
                    #country='th'
                    #vnname = u'Bệnh viện'.encode('utf-8')
                    #input = input.replace('hospital', vnname).replace('Hospital', vnname).replace('HOSPITAL', vnname)
                    item={}
                    if input not in self.url_set:

                        item['input']=input
                        item['location']=location
                        item['country']=country
                        settings = get_project_settings()
                        key = settings['KEY4']
                        base_url = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?input=' + input + '&types=establishment&key='+key+'&components=country:' + country
                        request = Request(base_url,callback=self.parse_placeids,meta={"item":item})
                        #print item
                        request_list.append(request)
                    else:
                        print 'has been in mysql=='
        return request_list


    def parse_placeids(self, response):
        html = response.body
        data = json.loads(html)
        item=response.meta['item']
        input=item['input']
        country=item['country']
        location=item['location']
        status = data['status']
        if status not in ['OK','ZERO_RESULTS']:
            raise Exception()
        predictions = data['predictions']
        place_id_count=len(predictions)
        if place_id_count>0:
            placeitem=PlaceIdItem()
            for prediction in predictions:
                description = prediction['description']
                place_id = prediction['place_id']
                placeitem['description']=description
                placeitem['place_id'] =place_id
                placeitem['input'] =input
                placeitem['country'] =country
                placeitem['location'] =location
                placeitem['status'] = status
                placeitem['place_id_count']=str(place_id_count)
                #print placeitem
                yield placeitem
        else:
            placeitem = PlaceIdItem()
            placeitem['input'] = input
            placeitem['country'] = country
            placeitem['location'] = location
            placeitem['place_id'] = '---'
            placeitem['status'] = status
            placeitem['place_id_count'] = str(place_id_count)
            yield placeitem
            #print placeitem






