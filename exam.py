examMark = int(input("Please enter exam mark: "))
totalMark = int(input("Please enter total marks on exam: "))

examPercent = float(examMark/totalMark)*100

if examPercent < 40:
    examResult = "Fail"
elif examPercent >= 70:
    examResult = "1:1"
elif examPercent >= 60:
    examResult = "2:1"
elif examPercent >= 50:
    examResult = "2:2"
elif examPercent >= 40:
    examResult = "3:3"

print("Congratulations. Your result is " + examResult)

    
    
