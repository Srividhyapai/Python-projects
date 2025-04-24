#Tip calculator

print("Welcome to Tip Calculator")
total_bill = float(input("What was your total bill?"))
tipping_amt = float(input(" How much tip would you like to give? 10, 12 or 15?"))
Heads_split = float(input ( "How many people to split the bill?"))
tip = tipping_amt/100
tip_as_percent = total_bill * tip
overall_total_bill = total_bill + tip_as_percent
total_split_per_head = round((overall_total_bill / Heads_split),2)
print(f"Each person has to pay: {total_split_per_head}")
