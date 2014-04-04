'''
Created on Mar 30, 2014

@author: Abhinav
'''
from freebaseUtil import getTopPropertyLevel, getCompoundPropertyList
from printUtil import printEndLine, printLine, printDescLine, printMainHeading, setPrintSpacing

leaguePropDict = {'Name':'/type/object/name',
                  'Sport':'/sports/sports_league/sport', 
                   'Slogan':'/organization/organization/slogan','Official Website':'/common/topic/official_website',
                   'Championship':'/sports/sports_league/championship', 
                  'Teams':{'top':'/sports/sports_league/teams','property':['/sports/sports_league_participation/team']},
                              'Description':'/common/topic/description'
                  }

inputJson = ''
line_len = 79

def printLeagueInfo(topicJson,header):
    global inputJson
    inputJson = topicJson
    setPrintSpacing(17,line_len)
    printNameAndHeader(header)
    printSport()
    printSlogan()
    printWebSite()
    printChampionship()
    printTeams()
    printDescription()
    

def printNameAndHeader(header):
    name = getTopPropertyLevel(inputJson,leaguePropDict['Name'])
    if name == None:
        return
    printMainHeading(name[0]+header)
    printLine('Name', name[0])
    printEndLine()

def printSport():
    sport = getTopPropertyLevel(inputJson,leaguePropDict['Sport'])
    if sport == None:
        return
    printLine('Sport', sport[0])
    printEndLine()

def printSlogan():
    slogan = getTopPropertyLevel(inputJson,leaguePropDict['Slogan'])
    if slogan == None:
        return
    printLine('Slogan', slogan[0])
    printEndLine()

def printWebSite():
    sport = getTopPropertyLevel(inputJson,leaguePropDict['Official Website'])
    if sport == None:
        return
    printLine('Official Website', sport[0])
    printEndLine()

def printChampionship():
    slogan = getTopPropertyLevel(inputJson,leaguePropDict['Championship'])
    if slogan == None:
        return
    printLine('Championship', slogan[0])
    printEndLine()

def printDescription():
    desc = getTopPropertyLevel(inputJson,leaguePropDict['Description'])
    if desc == None:
        return
    lineList = [desc[0][i:i+line_len] for i in range(0, len(desc[0]), line_len)]
    printDescLine('Description', lineList[0])
    for i in range (1,len(lineList)):
        printDescLine('', lineList[i])
    printEndLine()

def printTeams():
    listOfTeams = getCompoundPropertyList(inputJson,leaguePropDict['Teams']['top'], leaguePropDict['Teams']['property'])
    if listOfTeams == None:
        return
    printLine('Teams',listOfTeams[0][0])
    for i in range (1,len(listOfTeams)):
        printLine('',listOfTeams[i][0])
    printEndLine()
         

