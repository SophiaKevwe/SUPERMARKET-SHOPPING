#(GENESIS SUPERMARKET)
print("Welcome to Genesis Pizza Delivery")
print("SMALL SIZE = N1500 \n-PEPPERONI = N200 \nMEDIUM SIZE = N2000 \n-PEPPERONI = N300 \nLARGE SIZE = N2500 \n-PEPPERONI = N300 \nEXTRA CHEESE = N100")
sizep = input("What size of pizza do you want, S, M or L :")
add_pepperoni = input("Do you want pepperoni, Y or N :")
extra_cheese = input("Do you want extra cheese, Y or N :")
bill =0
total =0
if sizep.upper() == "S":
    bill = 1500
    if add_pepperoni.upper() == "Y":
        bill = bill + 200
    if extra_cheese.upper() == "Y":
        bill = bill + 100
elif sizep.upper() == "M":
    bill = 2000
    if add_pepperoni.upper() == "Y":
        bill = bill + 300
    if extra_cheese.upper() == "Y":
        bill = bill + 100
elif sizep.upper() == "L":
    bill = 2500
    if add_pepperoni.upper() == "Y":
        bill = bill + 300
    if extra_cheese.upper() == "Y":
        bill = bill + 100
else:
    print("INVALID INPUT")
total = bill
if add_pepperoni.upper() == "Y" and extra_cheese.upper() == "Y":
    print("Your bill is N", total,"with pepperoni and extra cheese")
elif add_pepperoni.upper() == "Y" and extra_cheese.upper() == "N":
    print("Your bill is N", total,"with pepperoni")
elif add_pepperoni.upper() == "N" and extra_cheese.upper() == "Y":
    print("Your bill is N", total,"with extra cheese")
elif add_pepperoni.upper() == "N" and extra_cheese.upper() == "N":
    print("Your bill is N",total)



