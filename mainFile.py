import sys
import re
from optparse import OptionParser
import QuestionAnswer
import infoboxMain
class MyOptionParser(OptionParser):
    def error(self, msg):
        error = """1. --key <account_key> -q <query> -t [infobox|question]
                If the type is infobox (i.e., -t infobox) the system tries to find the most relevant entity to the query <query> and create an infobox about it.
                If the type is question (i.e., -t question), the system tries to answer the question if it is of type "Who created [X]?".
                Note that the query has to be given as a single parameter.
                2. --key <account_key> -f <file_with_queries> -t [infobox|question]
                If the type is infobox (i.e. -t infobox) the system read the file <file_with_queries> an treat each line as a query for infox creation.
                If the type is question (i.e., -t question), the system treats each line of the <file_with_queris> files as a "Who created [X]?" question and tries to answer it.
                Note that the file name has to be given as a single parameter. """
        print error 
        sys.exit(0)


def main():
    parser = MyOptionParser()
    parser.add_option("--key", dest="key")
    parser.add_option("-q", dest="query")
    parser.add_option("-f", dest="fileName")
    parser.add_option("-t",  dest="queryType")
    (options, args) = parser.parse_args()
    key =  options.key
    query =  options.query
    queryType = options.queryType
    fileName = options.fileName

    if query and fileName:
        parser.error('error')
        
    if not key or not (query or fileName) or not queryType:
        parser.error('error')

    if query:
        if queryType == "infobox":
            infoboxMain.infoboxHelper(key, query)
        elif queryType == "question":
            query = query.lower()
            creationObj = re.match(r'who created (.*)\?', query)
            #print creationObj.group(1)
            if creationObj==None:
                print "Wrong question!!!"
                sys.exit(0)     
            creation = creationObj.group(1)
            if creation.strip()=="":
                print "Wrong question!!!"
                sys.exit(0)
            
            QuestionAnswer.questionAnswering(key, creation)
        else:
            parser.error('error')
    elif fileName:
        if queryType == "infobox":
            f = open(fileName)
            for line in f:
                strmsg = 'Query-Question: ' + line
                print strmsg
                infoboxMain.infoboxHelper(key, line)
            f.close()
        elif queryType == "question":
            f = open(fileName)
            for line in f:
                strmsg = 'Query-Question: ' + line
                print strmsg
                creationObj = re.match(r'who created (.*)\?', line.lower())
                if creationObj==None:
                    print "Wrong question!!!"
                    sys.exit(0)     
                creation = creationObj.group(1)
                if creation.strip()=="":
                    print "Wrong question!!!"
                    sys.exit(0)
                QuestionAnswer.questionAnswering(key, creation)
            f.close()
        else:
            parser.error('error')

         
            
            
            
    
    

if __name__ == "__main__":
    main()

