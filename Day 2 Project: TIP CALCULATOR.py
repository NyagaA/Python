									# TIP CALCULATOR PROJECT
# Round the result to 2 decimal places eg. $36.30

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))


tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = tip_amount + bill
bill_per_person = total_bill / people

#Rounding to 2 decimal places
payment = round(bill_per_person ,2)  
payment = "{:.2f}".format(bill_per_person)  #this formatting helps when the payment results to only 1 											  decimal even after using the round function

print(f"Each person should pay: ${payment}")
