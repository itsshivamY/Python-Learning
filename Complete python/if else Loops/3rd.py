CGPA = int(input("Enter your CGPA in this year:- "))

if CGPA >= 101:
    print("Please verify your CGPA again")
    exit()
if CGPA >= 90:
    grade = "A"
elif CGPA >= 80:
    grade = "B"
elif CGPA >= 70:
    grade = "C"
elif CGPA >= 60:
    grade = "D"
else:
    grade = "F"
print("Your Grade is:- ",grade)
