import urllib
import urllib2
import json

def search_api(query,key):
    #inputQuery = 'Bill Gates'
    inputQuery = urllib.quote(query);
    #key = 'AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY'
    #param = { 'query' : inputQuery, 'key' : key}   
    fblink = 'https://www.googleapis.com/freebase/v1/search?query=' + inputQuery + '&key=' + key
    print fblink
    req = urllib2.Request(fblink)
    response = urllib2.urlopen(req)
    content = response.read()
    #content contains the json response from freebase.
    json_result = json.loads(content)
    #print json_result
    return json_result

def topic_api(mid, key):
    #inputQuery = 'Bill Gates'
    #inputQuery = urllib.quote(query);
    key = 'AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY'
    #param = { 'query' : inputQuery, 'key' : key}   
    fblink = 'https://www.googleapis.com/freebase/v1/topic/' + mid + '?key=' + key
    print fblink
    req = urllib2.Request(fblink)
    response = urllib2.urlopen(req)
    content = response.read()
    #content contains the json response from freebase.
    json_result = json.loads(content)
    #print json_result
    return json_result