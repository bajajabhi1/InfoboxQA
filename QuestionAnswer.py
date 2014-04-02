import re
import urllib
import urllib2
import json

def questionAnswering():
    query = "Who created lord of the rings?"
    creationObj = re.match(r'Who created (.*)\?', query)
    creation = creationObj.group(1)

    api_key = "AIzaSyAIB0OSE8CQ4yETwSFefsMh0_k1RMnT2k4"
    mqlQuery = [{"type": "/book/written_work", "author": [],"name~=": creation, "a:name": None }]
    params = {
            'query':json.dumps(mqlQuery),
            'key': api_key
            }
    
    service_url = 'https://www.googleapis.com/freebase/v1/mqlread'

    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    #print response['result']
    for entry in response['result']:
        if entry['author']:
            print entry['a:name']+' written by ' + ', '.join(entry['author'])

    mqlQuery = [{"type": "/organization/organization", "founders": [], "name~=": "microsoft", "a:name": None}]
    params = {
            'query':json.dumps(mqlQuery),
            'key': api_key
            }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    #print response['result']
    for entry in response['result']:
        if entry['founders']:
            print entry['a:name']+' founded by ' + ', '.join(entry['founders'])


    
    
    
questionAnswering()
