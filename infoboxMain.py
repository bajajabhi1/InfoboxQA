'''
Created on Mar 30, 2014

@author: Abhinav
'''
import sys
from Person import printPersonInfo
from Author import printAuthorInfo
from freebaseUtil import search_api, topic_api
from Actor import printActorInfo
from BussPerson import printBussPerInfo
from League import printLeagueInfo
from SportsTeam import printSportsTeamInfo

key = ''
personTypeList = ['/people/person']
authorTypeList = ['/book/author']
actorTypeList = ['/film/actor', '/tv/tv_actor']
bussPersonTypeList = ['/organization/organization_founder', '/business/board_member']
leagueTypeList = ['/sports/sports_league']
sportsTeamTypeList = ['/sports/sports_team', '/sports/professional_sports_team']
entityTypes = personTypeList + authorTypeList + actorTypeList + bussPersonTypeList + leagueTypeList + sportsTeamTypeList

authorPropList = ['/book/author']
actorPropList = ['/film/actor', '/tv/tv_actor']
bussPersonPropList = ['/organization/organization_founder', '/business/board_member']
leaguePropList = ['/sports/sports_league']
sportsPropList = ['/sports/sports_team', '/sports/professional_sports_team']
    

def infoboxHelper(keyLocal, query):
    global key
    key = keyLocal
    
    # search the query
    search_result = search_api(query,key)
    #print search_result
    # find all the mids from the initial query
    midList = search_mids(search_result)
    # the mids from this result should be filtered for having one of the 6 entity types given
    # take the top relevant mid and search for it        
    # find all the 6 entity types in this entity
    [mid, topicJson, types] = search_top_topic(midList)
    print mid
    #print topicJson
    if mid == None:
        print 'No relevant type found for this query'
        sys.exit()
    
    #print mid
    #print types
    # Get all the Properties Of Interest of each entity types
    # Create the infobox output
    headerStr = getHeader(types)
    isPerson = False
    isActor = False
    isBussPerson = False
    isTeam = False    
    for type in types:
        if type in personTypeList:
            printPersonInfo(topicJson,headerStr)
            isPerson = True
    for type in types:
        if type in actorTypeList:
            if isActor == False and isPerson == True:
                printActorInfo(topicJson)
                isActor = True
    for type in types:
        if type in authorTypeList:
            if isPerson == True:
                printAuthorInfo(topicJson)
    for type in types:
        if type in bussPersonTypeList:
            if isBussPerson == False and isPerson == True:
                printBussPerInfo(topicJson)
                isBussPerson = True
    if isPerson == False:
        for type in types:
            if type in sportsTeamTypeList:
                if isTeam == False:
                    printSportsTeamInfo(topicJson,headerStr)
                    isTeam = True
    if isPerson == False and isTeam == False:
        for type in types:
            if type in leagueTypeList:
                printLeagueInfo(topicJson,headerStr)

def getHeader(types):
    headerStr = '('
    isPerson = False
    isActor = False
    isBussPerson = False
    isTeam = False
    for type in types:
        if type in personTypeList:
            isPerson = True    
    for type in types:
        if type in actorTypeList:
            if isActor == False and isPerson == True:
                headerStr = headerStr + 'ACTOR, '
                isActor = True
    for type in types:
        if type in authorTypeList:
            if isPerson == True:
                headerStr = headerStr + 'AUTHOR, '
    for type in types:
        if type in bussPersonTypeList:
            if isBussPerson == False  and isPerson == True:
                headerStr = headerStr + 'BUSINESS_PERSON, '
                isBussPerson = True
    if isPerson == False:
        for type in types:
            if type in sportsTeamTypeList:
                if isTeam == False:
                    headerStr = headerStr + 'SPORTS TEAM, '
                    isTeam = True
    if isPerson == False and isTeam == False:
        for type in types:
            if type in leagueTypeList:
                headerStr = headerStr + 'LEAGUE, '
    if headerStr[len(headerStr)-2] == ",":
        headerStr = headerStr[0:len(headerStr)-2]        
    return headerStr + ')'

def search_mids(search_result):
    resultList = search_result['result']
    midList = []
    for result in resultList:
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

