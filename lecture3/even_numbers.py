# reads a number k from the user
# outputs all even numbers in their own line
# from 1 to k (inclusively)

k = int(input("What is k?"))
for number in range(1, k+1):
    if number % 2 == 0:
        print(number)