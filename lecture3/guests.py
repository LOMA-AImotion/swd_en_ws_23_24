guests = []

guest_command = input("Who do you want to invite? Type <nobody> to stop.")
while guest_command != "nobody": 
  guests.append(guest_command)
  guest_command = input("Who do you want to invite? Type <nobody> to stop.")

print("Got it. All guests: ", guests)
print("These are " + str(len(guests)) + " people.")


