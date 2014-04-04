'''
Created on Mar 30, 2014

@author: Abhinav
'''
from freebaseUtil import getTopPropertyLevel, getCompoundPropertyList, getCompoundPropertyListMulti
from printUtil import *

sportsTeamPropDict = {'Name':'/type/object/name', 'Sport':'/sports/sports_team/sport',
                  'Arena':'/sports/sports_team/arena_stadium', 'Championships':'/sports/sports_team/championships',
                   'Founded':'/sports/sports_team/founded', 'Locations':'/sports/sports_team/location',
                  'Leagues':{'top':'/sports/sports_team/league','property':['/sports/sports_league_participation/league']},
                  'PlayersRoster':{'top':'/sports/sports_team/roster', 'property':['/sports/sports_team_roster/player',
                                    '/sports/sports_team_roster/position', '/sports/sports_team_roster/number',
                                    '/sports/sports_team_roster/from', '/sports/sports_team_roster/to']},
                  'Coaches':{'top':'/sports/sports_team/coaches', 'property':['/sports/sports_team_coach_tenure/coach',
                                    '/sports/sports_team_coach_tenure/position','/sports/sports_team_coach_tenure/from',
                                    '/sports/sports_team_coach_tenure/to']},
                  'Description':'/common/topic/description'}

inputJson = ''

def printSportsTeamInfo(topicJson,header):
    global inputJson
    inputJson = topicJson
    printNameAndHeader(header)
    printSingle('Sport')
    printSingle('Arena')
    printMultiple('Championships')
    printSingle('Founded')
    printLeagues()
    printSingle('Locations')
    printCoaches()
    printPlayers()
    printDescription()

def printNameAndHeader(header):
    name = getTopPropertyLevel(inputJson,sportsTeamPropDict['Name'])
    if name == None:
        return
    printMainHeading(name[0]+header)
    printLine('Name', name[0])
    printEndLine()

def printSingle(tag):
    value = getTopPropertyLevel(inputJson,sportsTeamPropDict[tag])
    if value == None:
        return
    printLine(tag, value[0])
    printEndLine()

def printMultiple(tag):
    found = getTopPropertyLevel(inputJson,sportsTeamPropDict[tag])
    if found == None:
        return
    printLine(tag, found[0])
    for i in range (1,len(found)):
        printLine('', found[i])
    printEndLine()

def printDescription():
    desc = getTopPropertyLevel(inputJson,sportsTeamPropDict['Description'])
    if desc == None:
        return
    lineList = [desc[0][i:i+82] for i in range(0, len(desc[0]), 82)]
    printDescLineST('Description', lineList[0])
    for i in range (1,len(lineList)):
        printDescLineST('', lineList[i])
    printEndLine()

def printCoaches():
    listOfCoaches = getCompoundPropertyListMulti(inputJson,sportsTeamPropDict['Coaches']['top'], sportsTeamPropDict['Coaches']['property'])
    if listOfCoaches == None or listOfCoaches == []:
        return
    #print listOfCoaches
    printCoachHeading('Coaches',['Name','Position','From/To']);
    for coaches in listOfCoaches:
        #print players
        posStr = ''
        if type(coaches[1]) is list:
           posStr = combineListToStr(coaches[1])
        else:
            posStr = coaches[1]
        nameStr = ''
        if type(coaches[0]) is list:
           nameStr = combineListToStr(coaches[0])
        else:
            nameStr = coaches[0]
        tmpEntry = [nameStr, posStr]
        if coaches[2] == ['']:
            tmpEntry.append('')
        elif coaches[3] == [''] or coaches[3] == '':
            tmpEntry.append(combineListToStr(coaches[2]) + ' / ' + 'now')
        else:
            tmpEntry.append(combineListToStr(coaches[2]) + ' / ' + combineListToStr(coaches[3]))
        printCoachEntry(tmpEntry) 
    printEndLine()

def printPlayers():
    listOfPlayers = getCompoundPropertyListMulti(inputJson,sportsTeamPropDict['PlayersRoster']['top'], sportsTeamPropDict['PlayersRoster']['property'])
    #print listOfPlayers
    if listOfPlayers == None or listOfPlayers == []:
        return
    printPlayerHeading('PlayersRoster',['Name','Position','Number','From/To']);
    for players in listOfPlayers:
        #print players
        posStr = ''
        if type(players[1]) is list:
           posStr = combineListToStr(players[1])
        else:
            posStr = players[1]
        nameStr = ''
        if type(players[0]) is list:
           nameStr = combineListToStr(players[0])
        else:
            nameStr = players[0]
        noStr = ''
        if type(players[2]) is list:
           noStr = combineListToStr(players[2])
        else:
            noStr = players[2]
        tmpEntry = [nameStr, posStr,noStr]
        if players[3] == '':
            tmpEntry.append('')
        elif players[4] == '':
            tmpEntry.append(combineListToStr(players[4]) + ' / ' + 'now')
        else:
            tmpEntry.append(combineListToStr(players[3]) + ' / ' + combineListToStr(players[4]))
        printPlayerEntry(tmpEntry) 
    printEndLine()

def combineListToStr(listInput):
    if listInput == [] or listInput == '':
        return ''
    posStr = listInput[0]
    for i in range (1,len(listInput)):
        posStr = posStr +', '+ listInput[i]
    return posStr

def printLeagues():
    listOfLeagues = getCompoundPropertyList(inputJson,sportsTeamPropDict['Leagues']['top'], sportsTeamPropDict['Leagues']['property'])
    if listOfLeagues == None or listOfLeagues == []:
        return
    printLine('Leagues',listOfLeagues[0][0])
    for i in range (1,len(listOfLeagues)):
        printLine('',listOfLeagues[i][0])
    printEndLine()
