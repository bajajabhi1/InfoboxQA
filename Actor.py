'''
Created on Mar 30, 2014

@author: Abhinav
'''
from freebaseUtil import getCompoundPropertyList
from printUtil import printFilmHeading, printFilmEntry, printEndLine

actorPropDict = {'Films':{'top':'/film/actor/film', 
                          'property':['/film/performance/character','/film/performance/film']}}

inputJson = ''

def printActorInfo(topicJson):
    global inputJson
    inputJson = topicJson
    printFilms()

def printFilms():
    listOfFilms = getCompoundPropertyList(inputJson,actorPropDict['Films']['top'], actorPropDict['Films']['property'])
    if listOfFilms == None or listOfFilms == []:
        return
    printFilmHeading('Films',['Character','Film Name'])
    #print listOfFilms
    for film in listOfFilms:
        printFilmEntry(film)   
    printEndLine()

