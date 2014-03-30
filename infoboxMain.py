# -*- coding: utf-8 -*-
import sys
from freebaseUtil import *

key = ''
personTypeList = ['/people/person']
authorTypeList = ['/book/author']
actorTypeList = ['/film/actor', '/tv/tv_actor']
bussPersonTypeList = ['/organization/organization_founder', '/business/board_member']
leagueTypeList = ['/sports/sports_league']
sportsTeamTypeList = ['/sports/sports_team', '/sports/professional_sports_team']
entityTypes = personTypeList + authorTypeList + actorTypeList + bussPersonTypeList + leagueTypeList + sportsTeamTypeList

personPropList = ['/people/person']
authorPropList = ['/book/author']
actorPropList = ['/film/actor', '/tv/tv_actor']
bussPersonPropList = ['/organization/organization_founder', '/business/board_member']
leaguePropList = ['/sports/sports_league']
sportsPropList = ['/sports/sports_team', '/sports/professional_sports_team']
    

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
    global key
    key  = 'AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY'
    query = 'Bill Gates'
    # search the query
    search_result = search_api(query,key)
    # find all the mids from the initial query
    midList = search_mids(search_result)
    # the mids from this result should be filtered for having one of the 6 entity types given
    # take the top relevant mid and search for it
    [mid, topicJson, types] = search_top_topic(midList)
    if mid == None:
        print 'No relevant type found for this query'
        sys.exit()
    
    print mid
    print types
    
    # find all the 6 entity types in this entity
    # Get all the Properties Of Interest of each entity types
    # Create the infobox output

def search_mids(search_result):
    #ex = tmpRes[u'result'].encode("iso-8859-15", "replace")
    #print ex
    resultList = search_result['result']
    midList = []
    for result in resultList:
        print '============================='
        print result['mid']
        midList.append(result['mid'])
    return midList
        
def search_top_topic(midList):
    for mid in midList:
        types = []
        found = False
        result = topic_api(mid,key)
        values = result['property']['/type/object/type']['values']
        for value in values:
            type = value['id'].encode("iso-8859-15", "replace")
            if type in entityTypes:
                found = True
                types.append(type)
        #print types
        if found == True:
            break
    
    if found ==True:
        return mid,result,types
    else:
        return None

if __name__ == "__main__":
    main()
