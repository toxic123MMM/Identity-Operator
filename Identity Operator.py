x =36
if(type(x) is int):
    print("true")
else:
    print("false")

x=1.9
if(type(x) is not float):
    print("true")
else:
    print("false")


x=36
y=36
if(x is y):
    print("X and Y have same value")
y=2
if(x is not y):
    print("X and Y have different value")
