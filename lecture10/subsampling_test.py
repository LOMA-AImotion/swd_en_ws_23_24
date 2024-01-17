def subsampling_to_first_half(sensor):
    # take a list of sensor values
    # return every 2nd, for the first half 

    # sensor = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
    # should output [3.2, 2.8, 6.4]
    return sensor[ : 1 + (len(sensor) // 2) : 2]

def run_test(values, expected):
    actual = subsampling_to_first_half(values)
    if actual == expected:
        print("Fine")
    else:
        print(f"Error: got {actual} instead of {expected}")

if __name__ == "__main__":
    sensor = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
    run_test(sensor, [3.2, 2.8, 6.4])
    run_test([3.2, 10.0, 2.8, 4.5, 6.4], [3.2, 2.8])
    run_test([3.2, 10.0, 2.8], [3.2])
    run_test([3.2], [3.2])