'''
Created on Mar 30, 2014

@author: Abhinav
'''
lineLen = 108
first_pipe = 9
heading_end_line = 98
first_heading = 14
first_value = 15
last_value = 81
heading_line = '---------------------------------------------------------------------------------- '

def setPrintSpacing(first_val,last_val):
    global first_value
    first_value=first_val
    global last_value
    last_value = last_val
    
def printMainHeading(heading):
    printEndLine()
    if len(heading) > lineLen:
        heading = heading[0:lineLen-4] + '...'
    print "%s %s%s" % (str('|').rjust(first_pipe),str(heading).center(97),str('|'))
    printEndLine()
    
    
def printLine(key,value):
    if len(value) > 69:
        value = value[0:69] + '...'
    
    if key=='':
        print "%s %s %s%s" % (str('|').rjust(first_pipe),str('').ljust(first_value),str(value).ljust(last_value),str('|'))
    else :
        print "%s %s %s%s" % (str('|').rjust(first_pipe),str(key + ':').ljust(first_value),str(value).ljust(last_value),str('|'))

def printDescLine(key,value):
    value = value.replace("\n", "")
    if key=='':
        print "%s %s %s%s" % (str('|').rjust(first_pipe),str('').ljust(first_value),str(value).ljust(last_value),str('|'))
    else :
        print "%s %s %s%s" % (str('|').rjust(first_pipe),str(key + ':').ljust(first_value),str(value).ljust(last_value),str('|'))

def printDescLineST(key,value):
    value = value.replace("\n", "")
    if key=='':
        print "%s %s%s%s" % (str('|').rjust(first_pipe),str('').ljust(first_value),str(value).ljust(82),str('|'))
    else :
        print "%s %s%s%s" % (str('|').rjust(first_pipe),str(key + ':').ljust(first_value),str(value).ljust(82),str('|'))

def printFilmHeading(heading,itemList):
    if len(itemList[0]) > 34:
        itemList[0] = itemList[0][0:34].strip() + '...'
    if len(itemList[1]) > 36:
        itemList[1] = itemList[1][0:36].strip() + '...'
    print "%s %s %s%s %s %s%s" % (str('|').rjust(first_pipe),str(heading + ':').ljust(first_heading),str('|'),str(itemList[0]).ljust(38),str('|'),str(itemList[1]).ljust(40),str('|'))
    print "%s %s" % (str('|').rjust(first_pipe),str(heading_line).rjust(heading_end_line))

def printFilmEntry(itemList):
    if len(itemList[0]) > 34:
        itemList[0] = itemList[0][0:34].strip() + '...'
    if len(itemList[1]) > 36:
        itemList[1] = itemList[1][0:36].strip() + '...'
    print "%s %s %s%s %s %s%s" % (str('|').rjust(first_pipe),str('').ljust(first_heading),str('|'),str(itemList[0]).ljust(38),str('|'),str(itemList[1]).ljust(40),str('|'))

def printBussHeading(heading,itemList):
    if len(itemList[0]) > 21:
        itemList[0] = itemList[0][0:21].strip() + '...'
    if len(itemList[1]) > 12:
        itemList[1] = itemList[1][0:12].strip() + '...'
    if len(itemList[2]) > 13:
        itemList[2] = itemList[2][0:13].strip() + '...'
    if len(itemList[3]) > 14:
        itemList[3] = itemList[3][0:14].strip() + '...'
    print "%s %s %s%s %s %s %s %s %s %s%s" % (str('|').rjust(first_pipe),str(heading + ':').ljust(first_heading),str('|'),str(itemList[0]).ljust(23),str('|'),str(itemList[1]).ljust(15),str('|'),str(itemList[2]).ljust(16),str('|'),str(itemList[3]).ljust(18),str('|'))
    print "%s %s" % (str('|').rjust(first_pipe),str(heading_line).rjust(heading_end_line))

def printBussEntry(itemList):
    if len(itemList[0]) > 21:
        itemList[0] = itemList[0][0:21].strip() + '...'
    if len(itemList[1]) > 12:
        itemList[1] = itemList[1][0:12].strip() + '...'
    if len(itemList[2]) > 13:
        itemList[2] = itemList[2][0:13].strip() + '...'
    if len(itemList[3]) > 14:
        itemList[3] = itemList[3][0:14].strip() + '...'
    print "%s %s %s%s %s %s %s %s %s %s%s" % (str('|').rjust(first_pipe),str('').ljust(first_heading),str('|'),str(itemList[0]).ljust(23),str('|'),str(itemList[1]).ljust(15),str('|'),str(itemList[2]).ljust(16),str('|'),str(itemList[3]).ljust(18),str('|'))
 
def printPlayerHeading(heading,itemList):
    if len(itemList[0]) > 16:
        itemList[0] = itemList[0][0:13].strip() + '...'
    if len(itemList[1]) > 19:
        itemList[1] = itemList[1][0:17].strip() + '...'
    if len(itemList[2]) > 17:
        itemList[2] = itemList[2][0:14].strip() + '...'
    if len(itemList[3]) > 18:
        itemList[3] = itemList[3][0:15].strip() + '...'
    print "%s %s %s%s %s %s %s %s %s %s%s" % (str('|').rjust(first_pipe),str(heading + ':').ljust(first_heading),str('|'),str(itemList[0]).ljust(16),str('|'),str(itemList[1]).ljust(20),str('|'),str(itemList[2]).ljust(18),str('|'),str(itemList[3]).ljust(18),str('|'))
    print "%s %s" % (str('|').rjust(first_pipe),str(heading_line).rjust(heading_end_line))

def printPlayerEntry(itemList):
    if len(itemList[0]) > 16:
        itemList[0] = itemList[0][0:13].strip() + '...'
    if len(itemList[1]) > 19:
        itemList[1] = itemList[1][0:17].strip() + '...'
    if len(itemList[2]) > 17:
        itemList[2] = itemList[2][0:14].strip() + '...'
    if len(itemList[3]) > 18:
        itemList[3] = itemList[3][0:15].strip() + '...'
    print "%s %s %s%s %s %s %s %s %s %s%s" % (str('|').rjust(first_pipe),str('').ljust(first_heading),str('|'),str(itemList[0]).ljust(16),str('|'),str(itemList[1]).ljust(20),str('|'),str(itemList[2]).ljust(18),str('|'),str(itemList[3]).ljust(18),str('|'))

def printCoachHeading(heading,itemList):
    if len(itemList[0]) > 23:
        itemList[0] = itemList[0][0:20].strip() + '...'
    if len(itemList[1]) > 26:
        itemList[1] = itemList[1][0:24].strip() + '...'
    if len(itemList[2]) > 24:
        itemList[2] = itemList[2][0:21].strip() + '...'
    print "%s %s %s%s %s %s %s %s%s" % (str('|').rjust(first_pipe),str(heading + ':').ljust(first_heading),str('|'),str(itemList[0]).ljust(23),str('|'),str(itemList[1]).ljust(27),str('|'),str(itemList[2]).ljust(25),str('|'))
    print "%s %s" % (str('|').rjust(first_pipe),str(heading_line).rjust(heading_end_line))

def printCoachEntry(itemList):
    if len(itemList[0]) > 23:
        itemList[0] = itemList[0][0:20].strip() + '...'
    if len(itemList[1]) > 26:
        itemList[1] = itemList[1][0:24].strip() + '...'
    if len(itemList[2]) > 24:
        itemList[2] = itemList[2][0:21].strip() + '...'
    print "%s %s %s%s %s %s %s %s%s" % (str('|').rjust(first_pipe),str('').ljust(first_heading),str('|'),str(itemList[0]).ljust(23),str('|'),str(itemList[1]).ljust(27),str('|'),str(itemList[2]).ljust(25),str('|'))
   
def printEndLine():
    print str('-------------------------------------------------------------------------------------------------- ').rjust(lineLen)
