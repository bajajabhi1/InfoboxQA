'''
Created on Mar 30, 2014

@author: Abhinav
'''
from freebaseUtil import getTopPropertyLevel
from printUtil import printEndLine, printLine

authorPropDict = {'Books':'/book/author/works_written',
                  'Influenced By':'/influence/influence_node/influenced_by', 
                  'Books about':'/book/book_subject/works',
                   'Influenced':'/influence/influence_node/influenced'}

inputJson = ''

def printAuthorInfo(topicJson):
    global inputJson
    inputJson = topicJson
    printBooks()
    printInfluencedBy()
    printBooksAbout()
    printInfluenced()

def printBooks():
    books = getTopPropertyLevel(inputJson,authorPropDict['Books'])
    if books == None:
            return
    printLine('Books',books[0])
    for i in range (1,len(books)):
        printLine('', books[i])
    printEndLine()

def printInfluencedBy():
    infby = getTopPropertyLevel(inputJson,authorPropDict['Influenced By'])
    if infby == None:
        return
    printLine('Influenced By', infby[0])
    for i in range (1,len(infby)):
        printLine('', infby[i])
    printEndLine()

def printBooksAbout():
    booksAbout = getTopPropertyLevel(inputJson,authorPropDict['Books about'])
    if booksAbout == None:
        return
    printLine('Books about', booksAbout[0])
    for i in range (1,len(booksAbout)):
        printLine('', booksAbout[i])
    printEndLine()

def printInfluenced():
    inf = getTopPropertyLevel(inputJson,authorPropDict['Influenced'])
    if inf == None:
        return
    printLine('Influenced', inf[0])
    for i in range (1,len(inf)):
        printLine('', inf[i])
    printEndLine()

