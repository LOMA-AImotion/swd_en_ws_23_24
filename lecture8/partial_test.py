from functools import partial 

def addup(x, y, z):
    print(f"x = {x}, y = {y}, z = {z}")
    return x + y + 2*z

only_two = partial(addup, 10)
only_two(20, 30)