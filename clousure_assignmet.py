def f(x):
    def g(y=x):
        return y
    return g
a=5
b=1
h=f(a)
print(h(b))
"""

def f(x):
    def g(y=x):
        return y
    return g
a=5
b=1
h=f(a)
print(h(b))

"""
