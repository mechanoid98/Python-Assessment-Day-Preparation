i = 0
number = 0

while number < 1:
    inputVariable = int(input("Please enter the number you want to end at (1-100): "))
    if inputVariable > 100:
        print("Insert a valid number")
    elif inputVariable < 1:
        print("Insert a valid number")
    else:
        number = inputVariable
        break

for i in range(101):
    square = i * i
    print("Number = ", i, "Squared number = ", square)
    if i == number:
        break
    
   

