print("*****Check Leap year*****")
 
year = int(input("Enter any year:- "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year," is a leap year")
else:
    print("Year is not leap year ")

