li=[]
print("enter elements in list:\n")
for x in range(5):
    a=input()
    li.append(a)
print(li)


##########################list functions#####################################
print("list in sorted order:")
li.sort()
print(li)
print("count fuction:")
print("apple:",li.count("apple"))
print("index fuction:")
print(li.index("mango"))
print("pop fuction")
li.pop()
print("list after pop fuction:")
print(li)
print("append fuction")
print(li.append("litchi"))
print("list after append fuction")
print(li)
print("insert fuction")
li.insert(4,"peach")
print(" list after insert fuction")
print(li)
print("remove fuction")
li.remove("peach")
print("list after remove fuction")
print(li)
print("reverse fuction")
li.reverse()
print("list after reverse fuction")
print(li)
del li[1:4]
print(li)