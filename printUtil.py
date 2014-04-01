'''
Created on Mar 30, 2014

@author: Abhinav
'''

def printMainHeading(heading):
    printEndLine()
    if len(heading) > 108:
        heading = heading[0:104] + '...'
    print "%s %s%s" % (str('|').rjust(9),str(heading).center(97),str('|'))
    printEndLine()
    
    
def printLine(key,value):
    if len(value) > 69:
        value = value[0:69] + '...'
    
    if key=='':
        print "%s %s %s%s" % (str('|').rjust(9),str('').ljust(15),str(value).ljust(81),str('|'))
    else :
        print "%s %s %s%s" % (str('|').rjust(9),str(key + ':').ljust(15),str(value).ljust(81),str('|'))

def printDescLine(key,value):
    value = value.replace("\n", "")
    if key=='':
        print "%s %s %s%s" % (str('|').rjust(9),str('').ljust(15),str(value).ljust(81),str('|'))
    else :
        print "%s %s %s%s" % (str('|').rjust(9),str(key + ':').ljust(15),str(value).ljust(81),str('|'))

def printFilmHeading(heading,itemList):
    if len(itemList[0]) > 34:
        itemList[0] = itemList[0][0:34].strip() + '...'
    if len(itemList[1]) > 36:
        itemList[1] = itemList[1][0:36].strip() + '...'
    print "%s %s %s%s %s %s%s" % (str('|').rjust(9),str(heading + ':').ljust(14),str('|'),str(itemList[0]).ljust(38),str('|'),str(itemList[1]).ljust(40),str('|'))
    print str('---------------------------------------------------------------------------------- ').rjust(108)

def printFilmEntry(itemList):
    if len(itemList[0]) > 34:
        itemList[0] = itemList[0][0:34].strip() + '...'
    if len(itemList[1]) > 36:
        itemList[1] = itemList[1][0:36].strip() + '...'
    print "%s %s %s%s %s %s%s" % (str('|').rjust(9),str('').ljust(14),str('|'),str(itemList[0]).ljust(38),str('|'),str(itemList[1]).ljust(40),str('|'))

def printBussHeading(heading,itemList):
    if len(itemList[0]) > 21:
        itemList[0] = itemList[0][0:21].strip() + '...'
    if len(itemList[1]) > 12:
        itemList[1] = itemList[1][0:12].strip() + '...'
    if len(itemList[2]) > 13:
        itemList[2] = itemList[2][0:13].strip() + '...'
    if len(itemList[3]) > 14:
        itemList[3] = itemList[3][0:14].strip() + '...'
    print "%s %s %s%s %s %s %s %s %s %s%s" % (str('|').rjust(9),str(heading + ':').ljust(14),str('|'),str(itemList[0]).ljust(23),str('|'),str(itemList[1]).ljust(15),str('|'),str(itemList[2]).ljust(16),str('|'),str(itemList[3]).ljust(18),str('|'))
    print str('---------------------------------------------------------------------------------- ').rjust(108)

def printBussEntry(itemList):
    if len(itemList[0]) > 21:
        itemList[0] = itemList[0][0:21].strip() + '...'
    if len(itemList[1]) > 12:
        itemList[1] = itemList[1][0:12].strip() + '...'
    if len(itemList[2]) > 13:
        itemList[2] = itemList[2][0:13].strip() + '...'
    if len(itemList[3]) > 14:
        itemList[3] = itemList[3][0:14].strip() + '...'
    print "%s %s %s%s %s %s %s %s %s %s%s" % (str('|').rjust(9),str('').ljust(14),str('|'),str(itemList[0]).ljust(23),str('|'),str(itemList[1]).ljust(15),str('|'),str(itemList[2]).ljust(16),str('|'),str(itemList[3]).ljust(18),str('|'))
    
def printEndLine():
    print str('-------------------------------------------------------------------------------------------------- ').rjust(108)
