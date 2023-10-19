voting_age = 18
name = input("What's your name?")
age = int(input("How old are you?"))
diff = age - voting_age

if diff > 0:
    print(name, " you've been allowed to vote for ", diff, "years")
elif diff == 0:
    print(name, "This is your first time voting")
else:
    print(name, " you have to wait for ", abs(diff), " years")