def my_double(x):
    return 2*x

def my_triple(x):
    return 3*x

if input("Use double? (y|n)") == "y":
    function_variable = my_double
else: 
    function_variable = my_triple

print(function_variable(10))