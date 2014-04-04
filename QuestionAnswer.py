import re
import urllib
import urllib2
import json

import collections
def questionAnswering(api_key, creation):
    
    #api_key = "AIzaSyAIB0OSE8CQ4yETwSFefsMh0_k1RMnT2k4"

    mqlQuery = [{"works_written": [{ "a:name": None,"name~=": creation }], "id": None, "name": None, "type": "/book/author"}]
    #mqlQuery = [{"type": "/book/written_work", "author": [],"name~=": creation, "a:name": None }]
    params = {
            'query':json.dumps(mqlQuery),
            'key': api_key
            }


    service_url = 'https://www.googleapis.com/freebase/v1/mqlread'

    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    result = {}
    #print response['result']
    for entry in response['result']:
        written_works = ""
        n = len(entry['works_written'])
        
        conjunct = ""
        for works in entry['works_written']:
            written_works = written_works + conjunct+" <"+works['a:name']+">"
            n = n - 1
            if n == 1:
                conjunct = " and"
            else:
                conjunct = ","
               
        if written_works!= "":
            result[entry['name']] =  "(as Author) created"+ written_works

        

        
    mqlQuery = [{ "organizations_founded": [{ "a:name": None, "name~=": creation }], "id": None, "name": None, "type": "/organization/organization_founder"}]
    params = {
            'query':json.dumps(mqlQuery),
            'key': api_key
            }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    #print response['result']

    for entry in response['result']:
        
        companies = ""
        n = len(entry['organizations_founded'])
        conjunct = ""
        for org in entry['organizations_founded']:
            companies = companies + conjunct+" <"+org['a:name']+">"
            n = n-1
            if n==1:
                conjunct = " and"
            else:
                conjunct = ","
                
        if companies!="":
            result[entry['name']] = "(as Businessperson) created"+companies

    od = collections.OrderedDict(sorted(result.items()))
    
    count = 1
    for k, v in od.iteritems():
        print str(count)+". " + k, v
        count = count + 1

    


