'''
Created on Mar 30, 2014

@author: Abhinav
'''
import urllib
import urllib2
import json

def search_api(query,key):
    #inputQuery = 'Bill Gates'
    inputQuery = urllib.quote(query);
    #key = 'AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY'
    #param = { 'query' : inputQuery, 'key' : key}   
    fblink = 'https://www.googleapis.com/freebase/v1/search?query=' + inputQuery + '&key=' + key
    #print fblink
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
    #key = 'AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY'
    #param = { 'query' : inputQuery, 'key' : key}   
    fblink = 'https://www.googleapis.com/freebase/v1/topic/' + mid + '?key=' + key
    #print fblink
    req = urllib2.Request(fblink)
    response = urllib2.urlopen(req)
    content = response.read()
    #content contains the json response from freebase.
    json_result = json.loads(content)
    #print json_result
    return json_result

def getTopPropertyLevel(topicJson,value):
    propDict = topicJson['property']
    if value in propDict.keys():
        values = propDict[value]['values']
        if len(values) == 0:
            return None
        result = []
        for entry in values:
            if 'value' in entry.keys():
                val = entry['value'].encode("iso-8859-15", "replace")
                #print val
                result.append(val)
            else:
                val = entry['text'].encode("iso-8859-15", "replace")
                #print val
                result.append(val)
        return result
    else:
        return None

def getCompoundPropertyLevel(topicJson,value, value2):
    propDict = topicJson['property']
    if value in propDict.keys():
        values = propDict[value]['values']
        result = []
        for entry in values:
            if value2 in entry['property'].keys():
                valuesComp = entry['property'][value2]['values']
                for entryComp in valuesComp:
                    if 'value' in entryComp.keys():
                        val = entryComp['value'].encode("iso-8859-15", "replace")
                        #print val
                        result.append(val)
                    else:
                        val = entryComp['text'].encode("iso-8859-15", "replace")
                        #print val
                        result.append(val)
        return result
    else:
        return None

def getCompoundPropertyList(topicJson,topValue, value2List):
    propDict = topicJson['property']
    if topValue in propDict.keys():
        values = propDict[topValue]['values']
        result = []
        for entry in values:
            resEntry = []
            for value2 in value2List:
                if value2 in entry['property'].keys():
                    valuesComp = entry['property'][value2]['values']
                    if len(valuesComp) == 0:
                        resEntry.append('')
                        #print 'here1'
                    for entryComp in valuesComp:
                        if 'value' in entryComp.keys():
                            val = entryComp['value'].encode("iso-8859-15", "replace")
                            #print val
                            resEntry.append(val)
                        else:
                            val = entryComp['text'].encode("iso-8859-15", "replace")
                            #print val
                            resEntry.append(val)
                else:
                    resEntry.append('') # if info not available yet like case if marriage still going on
                    #print 'here2'
            result.append(resEntry)
        return result
    else:
        return None