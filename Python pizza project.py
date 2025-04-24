#Python pizza project

#source code:

print ("Welcome to python pizza")
size = input(" What size do you want? s, m or l")
pepparoni = input(" Do you want the pepparoni? y or n")
extra_cheese = input(" Do you want extra cheese? y or n")
pizza_prize = 0;
if size == "s":
    pizza_prize = 15
elif size == "m":
    pizza_prize = 20
elif size == "l":
    pizza_prize = 25
else:
    print("You have typed wrong input")
if(( pepparoni == "y") and (size == "s")):
    pizza_prize+=2
elif (( pepparoni == "y") and ((size == "m") or size == "l")):
    pizza_prize+=3
else:
    print("you have selected wrong input")
if((extra_cheese== "y")):
    pizza_prize+=1
    print (f"Your total bill {pizza_prize}")
else:
    print (f"Your total bill {pizza_prize}")


