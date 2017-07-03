# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
import logging
from scrapy import crawler
from scrapy.utils.project import get_project_settings

import MySQLdb.cursors

log = logging.getLogger('land')

class SQLStorePipeline(object):

    #数据库连接池
    def __init__(self):

        #print u'===================='
        settings = get_project_settings()
        ip= settings['MYSQL_IP']
        port= settings.get('MYSQL_PORT',3306)
        db=settings.get('MYSQL_DB','test')
        user=settings.get('MYSQL_USER','root')
        passwd=settings.get('MYSQL_PWD','')
        self.table=settings.get('DETAIL')


        self.dbpool = adbapi.ConnectionPool('MySQLdb', host=ip,db=db,
                user=user, passwd=passwd, cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)

    def make_insert_sql(self,item,table):
        sql1='replace into '+table+'('
        sql2=') values('
        col=''
        val=''
        param=[]
        for k,v in enumerate(item):
                col=col+v+','
                val=val+'%s'+','
                v1=item[v]
                v1=v1.replace("\\",'')
                v1=v1.replace("'",'')
                param.append(v1)
        sql= sql1+col[0:-1]+sql2+val[0:-1]+')'
        param=tuple(param)
        return (sql,param)


    #把item插入数据库，是在后台插入的
    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item


    def _conditional_insert(self, tx, item):
            #print u'正在插入。。'
            sql_param=self.make_insert_sql(item,self.table)
            sql2=sql_param[0]
            param=sql_param[1]
            #print sql2
            #print param
            tx.execute(sql2,param)
            #print 'Insert OK!'
            #log.info(u"插入成功!")
            print u'插入成功!'

    def handle_error(self, e):
        log.error(e)
        print e
