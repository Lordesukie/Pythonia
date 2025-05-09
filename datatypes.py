import random

#data types in Python deduced implicitly, you just assign the values to a specific variable name
#You can also specify the data type by writing the type in front of it, like name = str("Jade")
#The data types in python are:

data1 = 21 #int
data2 = "This is a String" #string
data3 = 200.8 #float
data4 = 1j #complex
data5 = ["Apple","Banana","Cherry"] #list
data6 = ("Eagle","Parrot","Penguin") #tuple
data7 = range(6) #range
data8 = {"name" : "John", "age" : 36} #dict
data9 = {"Purple", "White", "Gold"} #set
data10 = frozenset({"apple", "banana", "cherry"}) #frozenset
#data11 = true boolean
data12 = b"hello" #byte
data13 = bytearray(5) #byte array
data14 = memoryview(bytes(5))
data15 = None #none type


print(data1, data2, data3, data4, data5) 
print(random.randrange(1,10))
