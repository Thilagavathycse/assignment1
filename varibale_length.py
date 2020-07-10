#variable length argument
def variable_length(*marks):
    print("this is the sum of my mark:"+str(sum(marks)))
variable_length(10,10,10)#We can pass any number of argumets

