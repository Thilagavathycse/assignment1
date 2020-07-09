import re
expression="[+-]?([0-9]*[.])[0-9]+"
def regex_function(value):
    if(re.search(expression,value)):
        print("True")
    else:
        print("False")
if __name__ == '__main__' :
    value = "4"
regex_function(value)

value = "+5.000"
regex_function(value) 

value = "-6.95"
regex_function(value) 
value=".6"
regex_function(value)
	
