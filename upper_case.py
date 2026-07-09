names=['daksh','maheshwari']

def upper_case(name):
    return name.upper()

name_upper_case=map(upper_case,names)
print(list(name_upper_case))


name_upper_case=map(lambda name : name.upper(),names)
print(list(name_upper_case))