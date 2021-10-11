
print("Hello. Thank you for visiting our place. This is Tip Calculator")
bill = float(input("What was the total bill? $"))
percent = float(input("What percentage would you like to give? "))
people = float(input("How many people to spilt the bill? "))


bill_divide_percentage = (bill * percent) / 100
totalbill = bill + bill_divide_percentage
totalpay = totalbill / people
print(f"Each person should pay ${round(totalpay, 2)}")
