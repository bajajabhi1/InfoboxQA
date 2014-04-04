'''
Created on Mar 30, 2014

@author: Abhinav
'''
from freebaseUtil import getTopPropertyLevel, getCompoundPropertyList
from printUtil import printEndLine, printLine, printDescLine, printMainHeading

personPropDict = {'Name':'/type/object/name',
                  'Birthday':'/people/person/date_of_birth', 
                  'Death':['/people/deceased_person/date_of_death','/people/deceased_person/place_of_death','/people/deceased_person/cause_of_death'],
                   'Place of birth':'/people/person/place_of_birth','Description':'/common/topic/description', 
                  'Siblings':{'top':'/people/person/sibling_s','property':['/people/sibling_relationship/sibling']},
                  'Spouses':{'top':'/people/person/spouse_s', 'property':['/people/marriage/spouse','/people/marriage/from',
                                                                           '/people/marriage/to','/people/marriage/location_of_ceremony']}}

inputJson = ''

def printPersonInfo(topicJson,header):
    global inputJson
    inputJson = topicJson
    printNameAndHeader(header)
    printBirthday()
    printDeath()
    printPlaceOfBirth()
    printDescription()
    printSiblings()
    printSpouses()

def printNameAndHeader(header):
    name = getTopPropertyLevel(inputJson,personPropDict['Name'])
    if name == None:
        return
    printMainHeading(name[0]+header)
    printLine('Name', name[0])
    printEndLine()

def printBirthday():
    bday = getTopPropertyLevel(inputJson,personPropDict['Birthday'])
    if bday == None:
        return
    printLine('Birthday', bday[0])
    printEndLine()

def printDeath():
    deathDate = getTopPropertyLevel(inputJson,personPropDict['Death'][0])
    deathStr = ''
    if deathDate != None:
        deathStr = deathDate[0]
    
    deathPlace = getTopPropertyLevel(inputJson,personPropDict['Death'][1])
    if deathPlace != None:
        deathStr = deathStr + ' at ' + deathPlace[0]
    
    deathCause = getTopPropertyLevel(inputJson,personPropDict['Death'][2])
    if deathCause != None:
        deathStr = deathStr + ', cause: (' + deathCause[0]
        for i in range (1,len(deathCause)):
            deathStr = deathStr + ', ' + deathCause[i]
        deathStr = deathStr + ')'
    if deathStr == '':
        return
    printLine('Death', deathStr)
    printEndLine()

def printPlaceOfBirth():
    pob = getTopPropertyLevel(inputJson,personPropDict['Place of birth'])
    if pob == None:
        return
    printLine('Place of birth', pob[0])
    printEndLine()

def printDescription():
    desc = getTopPropertyLevel(inputJson,personPropDict['Description'])
    if desc == None :
        return
    lineList = [desc[0][i:i+81] for i in range(0, len(desc[0]), 81)]
    printDescLine('Description', lineList[0])
    for i in range (1,len(lineList)):
        printDescLine('', lineList[i])
    printEndLine()

def printSiblings():
    listOfsiblings = getCompoundPropertyList(inputJson,personPropDict['Siblings']['top'], personPropDict['Siblings']['property'])
    if listOfsiblings == None or listOfsiblings == []:
        return
    printLine('Siblings',listOfsiblings[0][0])
    for i in range (1,len(listOfsiblings)):
        printLine('',listOfsiblings[i][0])
    printEndLine()

def printSpouses():
    listOfSpouses = getCompoundPropertyList(inputJson,personPropDict['Spouses']['top'], personPropDict['Spouses']['property'])
    if listOfSpouses == None or listOfSpouses == []:
        return
    #print listOfSpouses
    spouseStr = ''
    for i in range (0,len(listOfSpouses)):
        spouse = listOfSpouses[i]
        spouseStr = spouse[0] + ' (' + spouse[1]
        if spouse[2] == '':
            spouseStr = spouseStr + ' - ' + 'now' + ')'
        else:
            spouseStr = spouseStr + '-' + spouse[2]+ ')'
        if spouse[3] != '':
            spouseStr = spouseStr + ' @ ' + spouse[3]
        if i==0:
            printLine('Spouses',spouseStr)
        else:
            printLine('',spouseStr)    
    printEndLine()         

