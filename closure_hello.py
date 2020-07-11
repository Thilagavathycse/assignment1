def function_outside():
    msg="Hi"
    def function_inside():
        nonlocal msg
 
        msg="Hello"
        print(msg)
    function_inside()
    print(msg)
function_outside()

"""
def print_msg(number):
    def printer():
        nonlocal number           
        number=3
        print(number)
    printer()
    print(number)
print_msg(9)


"""
