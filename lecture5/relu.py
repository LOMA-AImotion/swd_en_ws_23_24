# define the ReLU function
#   0 if x < 0
#   x if x > 0
# Print the values from -10 to 10

def relu(x : float) -> float:
    assert isinstance(x, (float, int))
    relu_value = None
    if x < 0:
        relu_value = 0
    else:
        relu_value = x
    return relu_value

for x in range(-10, 11):
    print("x:",x, "ReLU(x):", relu(x))