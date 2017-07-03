# -*- coding: utf-8 -*-

with open('mygirl','r') as rf:
    for line in rf:
        if line.strip()!="":
            print line.strip().split('\t')[0],
            print '----->',
            print line.strip().split('\t')[1],
            #print '--->',
            #print line.strip().split('\t')[2],
        print ''

