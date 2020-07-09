import re
expression="[A-Z]{5}[0-9]{4}[A-Z]{1}"
def regex_function(value):
    if(re.search(expression,value)):
        print("True")
    else:
        print("False")
if __name__ == '__main__' :
    value = "DECAA8056B"
regex_function(value)

value ="BWBPC6417P" 
regex_function(value) 

value ="JaMDD8000M"    
regex_function(value) 
value="XABJT54321"
regex_function(value)
