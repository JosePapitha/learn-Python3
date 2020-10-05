#creating lists with append function
mylist = []
mylist.append(1)
mylist.append(0)
mylist.append(0.3)
mylist.append("Jose")
#index of list is based on zero value
print(mylist)

for x in mylist:
	print(x)

#Basic operators

number = 1 + 2 * 3 / 4.0 # bodmas rule applies
print(number)

#power of number
squared = 2 ** 2
cubed = 3 ** 3
print(squared)
print(cubed)

#repeating sequence
heyhello = "hello " * 10
print(heyhello)

print([1,2,3] * 3)

#String Formats
name = "Jose"
print("Hello %s!" % name)

mylistvalue = [1,2,3]
print("Mylist is %s" %mylistvalue)

name = "Jose"
age = 23
print("%s is %d old!" % (name,age))

#String options
astring = "helloworld!"
print(len(astring))
print(astring.count("o"))
print(astring.index("e")) #index starts from 0
print(astring[3:7])
print(astring[3:7:2]) #skipping one character

#String Reverse
print(astring [::-1])




