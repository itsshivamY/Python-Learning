age = int(input("Enter your Age:- "))
print("Special offer for you because \n*****Today is Wednesday***** ")
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $",price)

