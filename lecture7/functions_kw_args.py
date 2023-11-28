def area(width:int, height:int, price:float = 1, net:bool = True) -> int:
    net_price = width * height * price
    if net:
        return net_price
    else:
        return net_price * 1.19

print(area(5,2))
print(area(5,2,2))
print(area(5,2, net=False))
print(area(5,2, price=5.0))