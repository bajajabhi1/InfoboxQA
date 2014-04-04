MAKEFILE
========
The project is in Python. 
Compile - No steps required

Run Command Options -
   
1. python main.py -key  <Freebase API key> -q <query> -t <infobox|question>  

NOTE: In case when query has multiple words then they should be in single quotes. For example,   
python main.py AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY -q 'bill gates' -t infobox 
 
2. python main.py -key <Freebase API key> -f <file of queries> -t <infobox|question>

NOTE: The question has multiple words so it should be in single quotes. For example,   
python main.py AIzaSyBuMq3W5wfLezCtWX9rIZXbGSXNtCCG7hY -q 'Who created Microsoft?' -t infobox