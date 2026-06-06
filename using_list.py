list1=["Daksh","Tanvi","Arun","Ritu"]
print(list1)
print(type(list1))
print(list1[2])
print(list1[0:3])
list1.append("abc")
list1[list1.index("abc")] = "xyz"
print(list1)