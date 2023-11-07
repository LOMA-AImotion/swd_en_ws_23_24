# Read an input k and create a set of tuples with i and i times "x"s
# ex: 
# k = 3
# out: {(1,"x"), (2, "xx"), (3, "xxx")}

k = int(input("What's k?"))
out_set = set([])
for i in range(1, k+1):
    xs = "x" * i
    tpl = (i, xs)
    out_set.add(tpl)

print(out_set)

# alternative with set comprehensions
out_set2 = { (i, "x"*i) for i in range(1, k+1)}
print(out_set2)