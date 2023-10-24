>>> friends = ["Rick", "Daryl"]
>>> friends
['Rick', 'Daryl']
>>> friends.append("Carl")
>>> friends
['Rick', 'Daryl', 'Carl']
>>> friends += ["Maggie"]
>>> friends
['Rick', 'Daryl', 'Carl', 'Maggie']
>>> friends.pop()
'Maggie'
>>> friends
['Rick', 'Daryl', 'Carl']
>>> friends.remove("Carl")
>>> friends
['Rick', 'Daryl']