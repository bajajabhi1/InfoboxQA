import re

def questionAnswering:
    query = "Who created microsoft?"
    creationObj = re.match(r'Who created (.*)\?', query)
    print creationObj.group(1)
