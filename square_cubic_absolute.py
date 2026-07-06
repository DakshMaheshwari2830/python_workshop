def sqaure(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x>=0:
        return x
    else:
        return -(x)
    
def higher_order_function(type):
    if type=='square':
        return sqaure
    elif type=='cube':
        return cube
    elif type=="absolute":
        return absolute

result=higher_order_function('square')
print(result(1060))
result=higher_order_function('cube')    
print(result(240))
result=higher_order_function('absolute')    
print(result(-3))