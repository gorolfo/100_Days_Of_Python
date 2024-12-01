##### DAY-2 CHALLENGE BEGIN #####
"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""

print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
percentage = int(tip) / 100
tip_amount = float(bill) * percentage
total_bill = float(bill) + round(tip_amount, 2)
people = input("How many people to split the bill? ")
split_bill = (float(total_bill) / int(people))
print(f"Each person should pay: ${round(split_bill,2)}")
##### DAY-2 CHALLENGE END #####