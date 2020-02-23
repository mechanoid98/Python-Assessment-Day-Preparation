#Declaring the list, list elements can be of different data types
myList = [1, 2, 3, 4, 5, "Hello"]

#Print the entire list
print(myList)
#You'll get [1, 2, 3, 4, 5, 'Hello']
print(myList[3])

#print the third item in the list (recall: Index starts from 0)
print(myList[-1])
#You'll get 3

#assign myList (from Index 1 to 4) to myList2 and print myList2
myList2 = myList[1:5]
print(myList2)
#You'll get [2, 3, 4, 5]

#modify the second item in myList and print the updated list
myList[1] = 20
print(myList)
#you'll get [1, 20, 3, 4, 5, 'Hello']

#append a new item to myList and print the updated list
myList.append("How are you?")
print(myList)
#you'll get [1, 20, 3, 4, 5, 'Hello', 'How are you?']

#remove the sixth item from myList and print the updated list
del myList[5]
print(myList)
#you'll get [1, 20, 3, 4, 5, 'How are you?]
