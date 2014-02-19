# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:47:49 2014

@author: princengoc
"""

#get long and latitudes by  hitting googlemap with queries

import urllib2
import os
import json
import codecs

os.chdir('/home/princengoc/cafehanoi')
f = codecs.open('dongda.jl', 'r', encoding='utf-8')
cafelist = json.load(f,encoding='utf-8')

prefix = "https://maps.googleapis.com/maps/api/geocode/json?address="
suffix = "&sensor=false"

#find the location of the given cafe
def findloc(cafe):
    add = reduce(lambda x,y: x+y, cafe['address']).encode('utf-8')
    pageurl = prefix + urllib2.quote(add) + suffix
    u = urllib2.urlopen(pageurl)
    content = u.read().decode('utf-8')
    jsonform = json.loads(content)
    dct = jsonform['results'][0]
    location = dct['geometry']['location']
    return location

#find addresses for all cafes on the list
for cafe in cafelist:
    location = findloc(cafe)
    cafe['location'] = location    

#write back to json file
f = codecs.open('dongdaloc.jl','wb',encoding='utf-8')
f.write(json.dumps(cafelist))
f.close()


#--- double check that this file works
#f = codecs.open('dongdaloc.jl', 'r', encoding='utf-8')
#cafelist = json.load(f,encoding='utf-8')
#findloc(cafelist[0])
#Ok! Seems to work.




    
    