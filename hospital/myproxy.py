# -*- coding: utf-8 -*-
# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random
from scrapy.utils.project import get_project_settings
import requests

# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    #settings = get_project_settings()
    daili_content=''

    def process_request(self, request, spider):
        print '=====request proxy=========='


        request.meta['proxy'] = 'https://192.168.2.90:1080'
        print u'ip为',
        print request.meta['proxy']

        #print request.headers['User-Agent']
        #request.meta['proxy'] = "http://"+'111.56.13.152:80'

        # Use the following lines if your proxy requires authentication
        #proxy_user_pass = "USERNAME:PASSWORD"
        proxy_user_pass=""
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass


