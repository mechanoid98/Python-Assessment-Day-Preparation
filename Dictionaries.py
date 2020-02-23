#declaring the dictionary, dictionary keys and data can be of different data types
myDict = {"One":1.35, 2.5:"Two point Five", 3:"+", 7.9:2}
#print the entire dictionary
print(myDict)
#You'll get {2.5: 'Two point Five', 3: '+', 'One': 1.35, 7.9: 2}
#Note that items in a dictionary are not stored in the same order as the way
#you declare them

#print the item with key = "One"
print(myDict["One"])
#You'll get 1.35

#print the item with key = 7.9
print(myDict[7.9])
#You'll get 2

#modify the item with key = 2.5 and print the updated dictionary
myDict[2.5] = "Two and a half"
print(myDict)

#You'll get {2.5: 'Two and a half', 3: '+', 'One': 1.35, 7.9: 2}
#add a new item and print the updated dictionary
myDict["New item"] = "I'm new"
print(myDict)

#remove the item with the key = "One" and print the updated dictionary
del myDict["One"]
print(myDict)

