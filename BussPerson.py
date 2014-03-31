'''
Created on Mar 30, 2014

@author: Abhinav
'''
from freebaseUtil import getCompoundPropertyList,getTopPropertyLevel
from printUtil import *

bussPersonPropDict = {'Founded':'/organization/organization_founder/organizations_founded', 
                  'Leadership':{'top':'/business/board_member/leader_of', 'property':['/organization/leadership/organization','/organization/leadership/role',
                                    '/organization/leadership/title','/organization/leadership/from', '/organization/leadership/to']},
                'Board Member':{'top':'/business/board_member/organization_board_memberships', 'property':['/organization/organization_board_membership/organization',
                                    '/organization/organization_board_membership/role', '/organization/organization_board_membership/title',
                                    '/organization/organization_board_membership/from', '/organization/organization_board_membership/to']}}

inputJson = ''

def printBussPerInfo(topicJson):
    global inputJson
    inputJson = topicJson
    printFounded()
    printLeadership()
    printBoardM()

def printFounded():
    found = getTopPropertyLevel(inputJson,bussPersonPropDict['Founded'])
    if found == None:
        return
    printLine('Founded', found[0])
    for i in range (1,len(found)):
        printLine('', found[i])
    printEndLine()
    
def printLeadership():
    listOfLeadership = getCompoundPropertyList(inputJson,bussPersonPropDict['Leadership']['top'], bussPersonPropDict['Leadership']['property'])
    #print listOfLeadership
    if listOfLeadership == None:
        return
    printBussHeading('Leadership',['Organization','Role','Title','From-To']);
    for leaders in listOfLeadership:
        tmpEntry = [leaders[0], leaders[1],leaders[2]]
        if leaders[3] == '':
            tmpEntry.append('')
        elif leaders[4] == '':
            tmpEntry.append('('+ leaders[3] + ' / ' + 'now' + ')')
        else:
            tmpEntry.append('('+ leaders[3] + ' / ' + leaders[4] + ')')
        printBussEntry(tmpEntry)   
    printEndLine()

def printBoardM():
    listOfMembership = getCompoundPropertyList(inputJson,bussPersonPropDict['Board Member']['top'], bussPersonPropDict['Board Member']['property'])
    #print listOfMembership
    if listOfMembership == None:
        return
    printBussHeading('Board Member',['Organization','Role','Title','From/To']);
    for members in listOfMembership:
        tmpEntry = [members[0], members[1],members[2]]
        if members[3] == '':
            tmpEntry.append('')
        elif members[4] == '':
            tmpEntry.append('('+ members[3] + ' / ' + 'now' + ')')
        else:
            tmpEntry.append('('+ members[3] + ' / ' + members[4] + ')')
        printBussEntry(tmpEntry) 
    printEndLine()

