
def outer(arg="outer"):
    return "outer"
print(outer())
def inner(arg1="inner"):
    return "inner"
print(inner())
def string():
    return "inside"
print(string())
print(inner())
print(outer())
