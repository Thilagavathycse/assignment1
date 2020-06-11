"""pass
It does nothing
it acts as a placeholder and makes the program syntactically correct.
for example,if i want to declare a function now,but i dont want to implement
it now.But in program,i cant leave the program(declaration alone) with out implementation.
In that sitiation, i can use pass statement to tell the program,TO DO NOTHING"
it will not raise an error.
its like comments in python but the difference is interpreter ignores the commands while
executing but pass key word tells the interpreter to do nothing.
we can define a class without arguments and functions and function also
syntax:
1.class sample: pass
2.def fun_tion(arguments):
    pass
"""
print("pass program output")
for i in range(0,10):
    if i%2==0:
        pass
    else:
        print(i)
