def num_zeros(values):
    """
    returns the number of occurrences
    of 0 in the list 
    """
    count_zeros = 0
    for i in range(1, len(values)):
        if values[i] == count_zeros:
            count_zeros += 1
            
    return count_zeros

if __name__ == "__main__":
    print(num_zeros([2, 0, 1, 0]))