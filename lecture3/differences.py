mt = [0, 1, 4, 5, 7, 8]
# should be [1, 3, 1, 2, 1]
differences = [ mt[i] - mt[i-1] for i in range(0, len(mt)) ]
print(differences)

differences = []
for i in range(1, len(mt)):
    differences.append(mt[i] - mt[i-1])

print(differences)