# -*- coding: utf-8 -*-
import urllib
import urllib2
import base64
import json
import sys

accountKey = ''

def main():
    #if len(sys.argv) != 4:
    #    print 'Running command is python main.py <bing account key> <precision> \'<query>\''
    #    sys.exit()
    
    #query = sys.argv[3]
    #targetPrec = sys.argv[2]
    #global accountKey
    #accountKey = sys.argv[1]
    #try:
    #    targetPrec = float(targetPrec)
    #    if targetPrec<=0.0 or targetPrec>1.0:
    #        print 'Please enter a valid precision value (0-1)'
    #        sys.exit()
    #except ValueError:
    #    print 'Please enter a valid precision value (0-1)'
    #    sys.exit()
    query = ''
    fb_search(query)

def fb_search(query):
    inputQuery = 'Lord of the Rings'
    inputQuery = urllib.quote(inputQuery);
    key = 'AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY'
    #param = { 'query' : inputQuery, 'key' : key}   
    fblink = 'https://www.googleapis.com/freebase/v1/search?query=' + inputQuery + \
             '&key=' + key
    print fblink
    req = urllib2.Request(fblink)
    response = urllib2.urlopen(req)
    content = response.read()
    #content contains the json response from Bing.
    json_result = json.loads(content)
    print json_result
    # the mids from this result should be filtered for having one of the 6 entity types given
    # take the top relevant mid and search for it
    # find all the 6 entity types in this entity
    # Get all the Properties Of Interest of each entity types
    # Create the infobox output

if __name__ == "__main__":
    main()
