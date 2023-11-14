# repeatedly ask a user if they want to add items to their shopping list
# If they do, ask them for name and quantity
# add that to a dictionary
# show dictionary
# show keys and values
# ----------------------------------------------
shopping_list = {}
item = str(input("Do you want to add an item (yes | no)?"))
while item == "yes":
    name = input("What do you want to buy?")
    quantity = int(input("How much do you want to buy?"))

    shopping_list[name] = quantity    
    item = str(input("Do you want to add another item (yes | no)?"))

print("You need to buy: ", shopping_list)
print("Keys: ", shopping_list.keys())
print("Values: ", shopping_list.values())