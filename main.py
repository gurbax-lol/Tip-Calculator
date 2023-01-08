#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_of_people = int(input("How many people to split the bill? "))

payable = total_bill * (float("1." + tip_percent))
payable_per_person = payable / no_of_people
formatted_amount = "{:.2f}".format(payable_per_person)
print(f"Each person should pay: ${formatted_amount}")
